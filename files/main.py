# main
from time import sleep
from boot import update

from ble_gateway import scanner

while True:
    sleep(10)
    print("updated for from github for 10 seconds")
    print("scanning")
    scanner()
