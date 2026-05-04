import pygame
import sys

#initialize pygame
pygame.init()

#set window dimensions
screen = pygame.display.set_mode((500, 650))

#main loop
running = True
while running:
    #handles events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
sys.exit()