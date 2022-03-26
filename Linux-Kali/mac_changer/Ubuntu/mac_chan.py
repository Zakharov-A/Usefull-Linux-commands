#!/usr/bin/env/ python

import subprocess

interface = "enp0s3"
new_mac = "00:11:22:33:44:55"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig enp0s3 down", shell=True)
# subprocess.call("ifconfig enp0s3 hw ether 00:11:22:33:44:55", shell=True)
# subprocess.call("ifconfig enp0s3 up", shell=True)
