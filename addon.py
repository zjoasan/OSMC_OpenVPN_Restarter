"""
    Plugin for Launching programs
"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon

# plugin constants
__plugin__ = "OSMC OpenVPN Restarter"
__author__ = "zjoasan"
__url__ = "https://openvpn.net/"
__git_url__ = "https://github.com/zjoasan/OsmcOpenVPNrestart"
__credits__ = "zjoasan"
__version__ = "0.0.1"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.OSMC_OpenVPN_Restarter')

output=os.popen("./vpnrestart.sh").read()


