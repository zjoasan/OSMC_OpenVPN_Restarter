#!/bin/bash
sudo systemctl stop openvpn
sleep 3
sudo systemctl start openvpn
exit

