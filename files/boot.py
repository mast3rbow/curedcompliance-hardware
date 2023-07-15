# Imports Libraries for OTA Updates
# Sets variables for libraries
import wifimgr
from time import sleep
import machine
import senko

try:
  import usocket as socket
except:
  import socket

def update():
    OTA = senko.Senko(user="mast3rbow", repo="curedcompliance-hardware", working_dir="files", files=["main.py", "wifimgr.py"])

    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

update()
