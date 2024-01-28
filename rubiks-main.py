#import modules
import pygame
pygame.init()

#create pygame screen
Screen_Width = 800
Screen_Height = 600
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))

#create game loop
run = True
while run:

    #create event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit        