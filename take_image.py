#Laura Poulton
#Dunni Adenuga
#HackHers 2016

import pygame
import pygame.camera
import pygame.image
from pygame.locals import *
import time

pygame.init()
pygame.camera.init()

#camera used is first available
cam = pygame.camera.Camera(camlist[0],(640,480))

def get_image(cam):     #takes image
    cam.start()
    image = cam.get_image()
    pygame.image.save(img, "sleepy_face.png")
    

def main():             #takes photo from webcam every minute
    take_photo = True
    while take_photo:
        events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    cam.stop()
                    take_photo = False

        get_image(cam)
        time.sleep(60)  #delays for one minute

    pygame.camera.quit()
        
