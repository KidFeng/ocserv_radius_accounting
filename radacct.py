#!/usr/bin/python

import os, socket
import pyrad.packet
from pyrad.client import Client
from pyrad.dictionary import Dictionary

server = "your_server_ip"
secret = "your_server_secret"
dict_path = "/path/to/dictionary"

srv = Client(server = server, secret = secret, dict=Dictionary(dict_path))
req = srv.CreateAcctPacket()
req["User-Name"] = os.getenv("USERNAME")
req["NAS-IP-Address"] = socket.gethostbyname(socket.gethostname())
req["NAS-Port"] = 0
req["Calling-Station-Id"] = os.getenv("IP_REAL")
req["Framed-IP-Address"] = os.getenv("IP_REMOTE")
req["Service-Type"] = "Framed-User"
req["Framed-Protocol"] = "AnyConnect"
req["Acct-Session-Id"] = os.getenv("ID")

if os.getenv("REASON") == "connect":
    req["Acct-Status-Type"] = "Start"
else:
    req["Acct-Status-Type"] = "Stop"
    req["Acct-Input-Octets"] = long(os.getenv("STATS_BYTES_IN"))
    req["Acct-Output-Octets"] = long(os.getenv("STATS_BYTES_OUT"))
    req["Acct-Session-Time"] = long(os.getenv("STATS_DURATION"))
    req["Acct-Terminate-Cause"] = "User-Request"

srv.SendPacket(req)
