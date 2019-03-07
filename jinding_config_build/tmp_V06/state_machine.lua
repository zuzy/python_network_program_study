#!/usr/bin/lua
local json = require("cjson")

local _menu_ = 'module/'
local _major_path_ = _menu_..'major.rule'
local _indep_path_ = _menu_..'indep.conf'
local _scene_path_ = _menu_..'scene.conf'
local _state_path_ = _menu_..'state.json'
local _depend_path_ = _menu_..'depends.conf'
local DISABLE = 'disable'
local TRAGER = 'trager'
local ON = 'on'
local OFF = 'off'

function F(state, name, action)
    local f = io.open(_major_path_)
    local major = json.decode(f:read())
    f:close()
    if state.name == DISABLE then
        return state
    else
        f = io.open(_depend_path_)
        local dep = json.decode(f:read())
        f:close()
    end
end

function state_machine(name)
    local f = io.open(_state_path_)
    local state = json.decode(f:read())
    local sce = {}
    f:close()
    if state[name] == DISABLE then
        print("disable", name)
        return state
    else
        f = io.open(_scene_path_)
        sce = json.decode(f:read(1024))
        f:close()
        if sce[name] then
            print("sce", name)
        else
            print("not a scene", name)
        end
    end
    return state
end

state_machine('摆风')
state_machine('照明二')
state_machine('洗浴场景')