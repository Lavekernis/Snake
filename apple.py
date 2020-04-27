import pygame
import os.path
import random

filepath = os.path.dirname(__file__)

class Apple():

    def __init__(self):
        self._X, self._Y = random.randint(0,79)*10,random.randint(0,59)*10
        self._appleImg = pygame.image.load(os.path.join(filepath,'apple.png'))

    @property
    def coordinates(self):
        return (self._X,self._Y)

    @coordinates.setter
    def coordinates(self,x,y):
        self._X = x
        self._Y = y

    def Eaten(self):
        self._X, self._Y = random.randint(0,79)*10,random.randint(0,59)*10

    def Draw_apple(self,screen):
        screen.blit(self._appleImg,(self._X,self._Y))