#!/usr/bin/evn/ python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interFace", dest="interFace", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interFace:
        parser.error("[-] Please specify an interface, use --help for more info.")#code to handle error
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options

def change_mac(interFace, new_mac):
    print("[+] Changing MAC address for" + interFace + " to " + new_mac)
    subprocess.call(["ifconfig", interFace, "down"])
    subprocess.call(["ifconfig", interFace, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interFace, "up"])

def get_current_mac(interFace):
    ifconfig_result = subprocess.check_output(["ifconfig", interFace])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
current_mac = get_current_mac(options.interFace)
print("Current MAC = " + str(current_mac))

change_mac(options.interFace, options.new_mac)

current_mac = get_current_mac(options.interFace)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed. ")


