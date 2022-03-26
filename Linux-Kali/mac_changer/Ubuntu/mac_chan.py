#!/usr/bin/env python

import subprocess

# interface = "enp0s3"
interface = input("interface > ")
# new_mac = "08:00:27:FA:04:DF"
# new_mac = "08:00:27:FA:04:33"
new_mac = input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call(" ifconfig " + interface + " down ", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call(" ifconfig " + interface + " up ", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

