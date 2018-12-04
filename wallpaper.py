import pygame
import sys
import random
import image
import itertools
from pygame.locals import *

surface_width = 1400
surface_height = 720
background_color =[0,0,255]

screen = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption("Wtf is this?")
my_clock = pygame.time.Clock()

def close():
    for event in pygame.event.get():
            if event.type is pygame.QUIT:
                sys.exit()
            elif event.type is KEYDOWN:
                sys.exit()
            else:
                pass
close

#if collides with the edge of screen, then changes the direction of the moving logo
def collision(sprites):

    for pair in itertools.product(sprites, repeat = 2):
    	print(type(pair[0]))
        if pair[0].rect.colliderect(pair[1].rect):
            for sprite in pair:
                sprite.reverseDir()

collision

#constantly changes background color after every event tick
def backgroundColor():

  # background_color[0] += random.randint(0,10)
    background_color[1] += random.randint(0,10)
    background_color[2] += random.randint(0,10)

    if background_color[0] > 255:
        background_color[0] = 0
    if background_color[1] > 255:
        background_color[1] = 0
    if background_color[2] > 255:
        background_color[2] = 0

backgroundColor

#moves the logo
def translate(sprite_list):
    maxX = 1200
    maxY = 700
    close()
    #first index stores position, second index stores direction
    for instance in sprite_list:
        instance.direction(maxX, maxY)

    #determines the direction of motion
    for instance in sprite_list:
        instance.update()
translate

#the main wallpaper event runs in this function, until the user exits it
def play(sprite_list, sound):
     while True:
        counter = 0
        event = pygame.event.poll()
        close()
   #     sound.play()
        screen.fill(background_color)
        for sprite in sprite_list:
           sprite.draw(screen)
        counter = random.randint(0, 1000000)
        if counter % 25 == 0:
            backgroundColor()
        translate(sprite_list)
        collision(sprite_list)
        pygame.display.flip()
play

#initializes the canvas, the background sound, and the objects
def main():
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('rain.wav')
    tux = image.image('Tux.png', screen)
    apple = image.image('apple.png', screen)
    sprite_list = [tux, apple]
    play(sprite_list, sound)
main()
