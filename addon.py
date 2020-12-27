"""
    Plugin for to stop and restart OpenVPN on OSMC-device
"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
import time

# plugin constants
__plugin__ = "OSMC OpenVPN Restarter"
__author__ = "Zjoasan"
__url__ = "https://osmc.tv/"
__git_url__ = "https://https://github.com/zjoasan/OSMC_OpenVPN_Restarter"
__credits__ = "Zjoasan"
__version__ = "0.0.2"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.OSMC_OpenVPN_Restarter')

os.system("sudo systemctl stop openvpn")
time.sleep(5)
os.system("sudo systemctl start openvpn")
dialog.ok("OpenVPN restart", "Now the system have stopped & started OpenVPN")


