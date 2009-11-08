---------------------------------------------------
-- Licensed under the GNU General Public License v2
--  * (c) 2009, Adrian C. <anrxc.sysphere.org>
--  * (c) Wicked, Lucas de Vries
--  moc plugin written by Zsolt Udvari <udvzsolt.gmail.com>
---------------------------------------------------

-- {{{ Grab environment
local io = { popen = io.popen }
local setmetatable = setmetatable
local helpers = require("vicious.helpers")
local string = {
    find = string.find,
    gsub = string.gsub,
    match = string.match
}

local print = print
-- }}}


-- Moc: provides the currently playing song in Moc
module("vicious.moc")


-- {{{ MOC widget type
local function worker(format)
    -- Get data from mocp
    local f = io.popen("mocp -i")
    local np = f:read("*all")
    local state = ""
    local artist = ""
    local title = ""
    local filename = ""
    local curtime = ""
    local totaltime = ""

    f:close()

    -- Check if it's stopped, off or not installed
    if np == nil then
        return {"STOP"}
    end

    state = string.match(np, "State: %a*")
    state = string.gsub(state,"State: ","")
    if state ~= "STOP" then
        artist = string.gsub(string.match(np,"Artist: %C*") or artist,"Artist: ","")
        title  = string.gsub(string.match(np,"SongTitle: %C*") or title,"SongTitle: ","")
        filename = string.gsub(string.match(np,"File: %C*") or filename,"File: ","")
        curtime = string.gsub(string.match(np,"CurrentTime: %d*:%d*") or curtime,"CurrentTime: ","")
        totaltime = string.gsub(string.match(np,"TotalTime: %d*:%d*") or totaltime,"TotalTime: ","")

        state = helpers.escape(state)
        artist = helpers.escape(artist)
        title = helpers.escape(title)
        filename = helpers.escape(filename)
        curtime = helpers.escape(curtime)
        totaltime = helpers.escape(totaltime)
    end

    return {state,artist,title,filename,curtime,totaltime}
end
-- }}}

setmetatable(_M, { __call = function(_, ...) return worker(...) end })
