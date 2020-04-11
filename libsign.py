# Libsign : A copyright string finder
# Author : r0da

import idautils
import os
import json
import re

print "Libsign : A copyright string finder"

sig = json.load(open(os.path.dirname(os.path.realpath(__file__)) + "\\db.json"))

for string in idautils.Strings():
    for signature in sig["signatures"]:
        if re.compile(signature["sig"]).search(str(string)):
            print "0x" + format(string.ea, 'x') + " : " + signature["name"] + " : " + signature["link"]
