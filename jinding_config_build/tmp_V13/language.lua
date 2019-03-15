require("en")
function state_transform(state)
    ret = {}
    for k, v in pairs(state) do
        ret[lang_tab[k]] = v
    end
    return ret
end