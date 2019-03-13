#!/usr/bin/lua
-- local json = require("cjson")
local json = require("cjson.safe")
sm = {}

local zone = -1
function dump_tab( tab )
    zone = zone + 1
    for k, v in pairs(tab) do
        local str = "\t"
        str = str:rep(zone)
        if type(v) == 'table' then
            print(str..k)
            dump_tab(v)
        else
            print(str..k, v)
        end
    end
    zone = zone - 1
end

function tab_update(tar, sub)
    if type(tar) == 'table' and type(sub) == 'table' then
        for ks, vs in pairs(sub) do
            tar[ks] = vs
        end
    end
    return tar
end

function list_extend(tar, sub)
    if type(tar) == 'table' and type(sub) == 'table' then
        for k, v in ipairs(sub) do
            table.insert(tar, v)
        end
    end
end

local _menu_ = 'module/'
local _major_path_ = _menu_..'major.rule'
local _indep_path_ = _menu_..'indep.conf'
local _scene_path_ = _menu_..'scene.conf'
local _state_path_ = _menu_..'state.json'
local _depend_path_ = _menu_..'depends.conf'
local _reset_path_ = _menu_..'reset.conf'
local DISABLE = 'disable'
local TRAGER = 'trager'
local ON = 'on'
local OFF = 'off'

local f = io.open(_major_path_)
local major = json.decode(f:read())
f:close()
f = io.open(_depend_path_)
local dep = json.decode(f:read())
f:close()
f = io.open(_indep_path_)
local indep = json.decode(f:read())
f:close()
f = io.open(_scene_path_)
local sce = json.decode(f:read())
f:close()
f = io.open(_reset_path_)
local reset = json.decode(f:read())
f:close()

local function _check_list_(tar_name, name)
    for n, v in ipairs(name) do
        if v == tar_name then
            return true
        end
    end
    return false
end

local function _check_tab_(tar_name, tab)
    for n, name in pairs(tab) do
        if (type(n) == 'string' and n == tar_name) or 
            (type(name) == 'string' and name == tar_name) then
            return true
        end
    end
    return false
end

local function check_indep(tar_name)
    return _check_tab_(tar_name, indep)
end

local function check_dep(tar_name)
    return _check_tab_(tar_name, dep)
end 

local function check_major(tar_name)
    return _check_tab_(tar_name, major)
end

local function check_scene(tar_name)
    return _check_tab_(tar_name, sce)
end

local function check_reset(tar_name)
    return _check_list_(tar_name,reset)
end

local function get_active_deps(state)
    
end

local function get_disable_deps(state)
    f = io.open(_depend_path_)
    local d = json.decode(f:read())
    f:close()
    tmp = {}
    -- print('check!!!!!!', json.encode(state))
    for chief, r in pairs(major) do
        if state[chief] == true then
            list_extend(tmp, r['deps'])
        end
    end
    -- print('dis !!!', json.encode(tmp))
    for n, t in pairs(tmp) do
        -- print(n, t)
        for nd, vd in pairs(d) do
            if t == vd then
                table.remove(d, nd)
                break
            end
        end
    end
    return d
end

local function deps_update(state, dis)
    f = io.open(_depend_path_)
    local dep = json.decode(f:read())
    f:close()
    for n, d in pairs(dep) do
        -- print('check', d)
        -- print("------!!!!------")
        -- dump_tab(dis)
        -- print("------!!!!------")
        if _check_list_(d, dis) then
            -- print("DISABLE", d)
            state[d] = DISABLE
        else
            -- print('Enable',d, state[d])
            if state[d] == DISABLE then
                state[d] = false
            end
            -- print(d, state[d])
        end
    end
    return state
end

local function major_rule(state, name, action)
    if action == nil then
        state[name] = not(state[name])
    else
        state[name] = action
    end
    rela = major[name]
    for chief, r in pairs(rela) do
        if state[chief] ~= nil and r == 'exclusive' then
            state[chief] = false
        end
    end
    d = get_disable_deps(state)
    state = deps_update(state, d)
    -- print('----------disable------------')
    -- dump_tab(d)
    -- print('----------disable------------')
    for nd, vd in pairs(d) do
        state[vd] = DISABLE
    end
end

local function F(state, name, action)
    -- print(name, state[name])
    if check_dep(name) then
        state[name] = not(state[name])
        -- state[name] = false
    elseif check_indep(name) then
        if action == nil then
            state[name] = not(state[name])
        else
            state[name] = action
        end
    elseif check_major(name) then
        -- print('major',name, '!!!!!!')
        major_rule(state,name,action)
        -- print(name, state[name])
    end
    return state
end

local function scene_check(state)
    for ks, vs in pairs(sce) do
        -- print(ks, vs)
        if state[ks] then
            -- print('true!!!')
            for n, v in pairs(vs) do
                -- print(n, v)
                if v and not state[n] then
                    -- print('find!!!')
                    state[ks] = false
                    break
                end
            end
        end
    end
    return state
end

local function batch_f(state, sce_name, action)
    sce_batch = sce[sce_name]
    if action == nil then
        state[sce_name] = not(state[sce_name]) 
    else
        state[sce_name] = action
    end
    for n, s in pairs(sce_batch) do
        if s then
            state = F(state, n, state[sce_name])
            -- print("!!!!!!", n)
            -- print('state', json.encode(state))

        end
    end
    return state
    
end

local function state_machine(name)
    local f = io.open(_state_path_)
    local state = json.decode(f:read())
    f:close()
    if state[name] == DISABLE then
        -- print("disable", name)
        return state
    else
        if check_reset(name) then
            -- print("reset!!!")
            for k, v in pairs(major) do
                if k ~= 'dependence' then
                    state[k] = false
                end
            end
            for n, k in ipairs(indep) do
                state[k] = false
            end
            for n, k in ipairs(dep) do
                state[k] = DISABLE
            end
            for k, v in pairs(sce) do
                state[k] = false
            end
        elseif check_scene(name) then
            if state[name] == false then
                for s, t in pairs(sce) do
                    if state[s] then
                        state = batch_f(state,s,false)
                    end
                end
            end
            batch_f(state,name,not(state[name]))
        else
            F(state, name, nil)
            scene_check(state)
            -- print("not a scene", name)
        end
    end
    -- print("---------state new--------")
    -- dump_tab(state)
    -- print("---------state new--------")
    f = io.open(_state_path_, 'w')
    s = json.encode(state)
    f:write(s)
    f:close()
    -- print(state)
    print(json.encode(state))
    return state
end

-- function sm.state_machine(name)
--     return state_machine(name)
-- end

-- state_machine('摆风')
-- return sm
-- state_machine('照明二')
-- state_machine('洗浴场景')
state_machine(arg[1])
-- print(os.clock())
-- print(arg[1])
-- state_machine('取暖')

-- a = {
--     ['a'] = 'sss',
--     ['b'] = 'ddd'
-- }
-- b = {
--     a = 'dfdf',
--     b,
--     1,
--     2,
--     3,
--     'a',
-- }
-- -- dump_tab( tab_update(a,b))
-- c = {
--     1,2,3
-- }
-- d = {
--     1,3,'sdf'
-- }
-- dump_tab(tab_update(c,d))