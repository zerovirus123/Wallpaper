import pygame
import random

surface_width = 1400
surface_height = 700
LEFT = 0
RIGHT = 1
UP = 0
DOWN = 1

class image(pygame.sprite.Sprite):

    def __init__(self,filename, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.x_cord = [random.randint(0,surface_width), random.randint(0,2)]
        self.y_cord = [random.randint(0,surface_height), random.randint(0,2)]
        self.rect = self.image.get_rect();

    def getImage(self):
        return self.image

    def getXCord(self):
        return self.x_cord[0]

    def getYCord(self):
        return self.y_cord[0]

    def getXDir(self):
        return self.x_cord[1]

    def getYDir(self):
        return self.y_cord[1]

    def setXCord(self, x_cord):
        self.x_cord[0] = x_cord

    def setYCord(self, y_cord):
        self.x_cord[0] = y_cord

    def setXDir(self, x_dir):
        self.x_cord[1] = x_dir

    def setYDir(self, y_dir):
        self.y_cord[1] = y_dir

    def direction(self, maxX, maxY):
        if self.x_cord[0] < 0:
           self.x_cord[0] = 0
           self.x_cord[1] = 1

        if self.x_cord[0] > maxX:
           self.x_cord[0] = maxX
           self.x_cord[1] = 0

        if self.getYCord() < 0:
           self.y_cord[0] = 0
           self.y_cord[1] = 1

        if self.getYCord() > maxY:
           self.y_cord[0] = maxY
           self.y_cord[1] = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x_cord[0], self.y_cord[0]))

    def reverseDir(self):
        if self.x_cord[1] is 1:
            self.x_cord[1] = 0;
        else:
            self.x_cord[1] = 1

        if self.y_cord[1] is 1:
            self.y_cord[1] = 0
        else:
            self.y_cord[1] = 1

    def update(self):
        if self.x_cord[1] is 1:
            self.x_cord[0] += 1
        else:
            self.x_cord[0] -= 1

        if self.y_cord[1] is 1:
            self.y_cord[0] += 1
        else:
            self.y_cord[0] -= 1


