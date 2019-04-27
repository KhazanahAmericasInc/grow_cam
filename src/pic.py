import pygame
import pygame.camera as camera
from time import sleep
import datetime

width = 800
height = 800
SLEEP_TIME = 900 #900

pygame.init()
camera.init()

cam = camera.Camera("/dev/video0",(width,height))
cam.start()
while(True):
    print("potato")
    #cam.start()
    img = cam.get_image()
    #cam.stop()
    dt = datetime.datetime.now()
    img_name = str(dt).replace(" ","_").replace(".","_")
    print(img_name,"saved")
    pygame.image.save(img, "captures/"+img_name+".jpg")
    sleep(SLEEP_TIME)
cam.stop()

