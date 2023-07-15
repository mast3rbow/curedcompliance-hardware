# main
import sleep
from boot import update

while True:
    print("latest github update")
    sleep(10)
    print("checking for an update")
    
    update()
