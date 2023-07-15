# Main

import wifimgr
import machine
import urequests
from utime import sleep

from ota import check_for_updates

# Loads into AP mode if not connected to WIFI
try:
    import usocket as socket
except:
    import socket
    
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

# Handles an Error where a Socket with AP stays open after device has been connected to WiFi
# machine reset() fixes this problem.
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(('', 80))
  s.listen(5)
except OSError as e:
  machine.reset()


while True:
    update = check_for_updates()
    print(update)
    sleep(5)



