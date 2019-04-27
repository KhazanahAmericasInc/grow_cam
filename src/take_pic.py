import pygame
import pygame.camera as camera

width = 800
height = 800

pygame.init()
camera.init()

cam = camera.Camera("/dev/video0",(width,height))
cam.start()
img = cam.get_image()
cam.stop()

pygame.image.save(img,"image.jpg")
