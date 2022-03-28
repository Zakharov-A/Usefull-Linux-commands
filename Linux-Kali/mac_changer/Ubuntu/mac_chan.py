#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")

parser.parse_args()

# interface = "enp0s3"
interface = input("interface > ")
# new_mac = "08:00:27:FA:04:DF"
# new_mac = "08:00:27:FA:04:33"
new_mac = input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

