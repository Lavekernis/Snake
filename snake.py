import pygame
import os.path

filepath = os.path.dirname(__file__)

class Snake():

    def __init__(self):
        self._node = [[400,310],[400,320]]
        self._head_X,self._head_Y = 800/2,600/2 
        self._direction = 'up'
        self._snakeImg = pygame.image.load(os.path.join(filepath,'node.png'))

    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self,a):
        self._direction = a
    
    @property
    def head_coordinates(self):
        return (self._head_X,self._head_Y)

    def Draw_snake(self,screen):
        screen.blit(self._snakeImg,(self._head_X,self._head_Y))
        for i in self._node:
            screen.blit(self._snakeImg,(i[0],i[1]))

    def Ruch(self):
        for i in range(1,len(self._node)+1):
            if i != len(self._node):
                self._node[-i][0],self._node[-i][1]=self._node[-i-1][0],self._node[-i-1][1]
            else:
               self._node[-i][0],self._node[-i][1]=self._head_X,self._head_Y 
        if self._direction == 'up':
            self._head_Y -= 10 
        elif self._direction == 'down':
            self._head_Y += 10
        elif self._direction == 'right':
            self._head_X += 10
        else:
            self._head_X -= 10 
        if self._head_X > 800:
            self._head_X = 0
        if self._head_X < 0:
            self._head_X = 790
        if self._head_Y > 600:
            self._head_Y = 0    
        if self._head_Y < 0:
            self._head_Y = 590               
    
    def Grow(self):
        self._node.append([self._node[-1][0],self._node[-1][1]])
    
    def Is_Crashing(self):
        for i in self._node:
            if i[0] == self._head_X and i[1] == self._head_Y:
                return True
        return False        
    
    def Restart_Snake(self):
        self._head_X,self._head_Y = 800/2,600/2
        self._node = [[400,310],[400,320]]
        self._direction = 'up'