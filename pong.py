#!/usr/bin/python2.7

import pygame

pygame.init()

#Set some variables
WIDTH=1200
HEIGHT=800
BORDER=20

#Draw the playing area
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bordercol = pygame.Color("white")

#Draw the board

##Define each rectangle which will be drawn to make up the border
rect1 = pygame.Rect((0,0),(WIDTH,BORDER))
rect2 = pygame.Rect((0,780),(WIDTH,BORDER))
rect3 = pygame.Rect((0,0),(BORDER,HEIGHT))
rect4 = pygame.Rect((1180,0),(BORDER,HEIGHT))

#Actually draw each rectangle to make the border
pygame.draw.rect(screen, bordercol, rect1)
pygame.draw.rect(screen, bordercol, rect2)
pygame.draw.rect(screen, bordercol, rect3)
pygame.draw.rect(screen, bordercol, rect4)

pygame.display.flip()