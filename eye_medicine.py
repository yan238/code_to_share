import transparent_window
from win32api import GetSystemMetrics

import random

import pygame
pygame.init()

screen = transparent_window.TransparentWindow.screen
pygame.display.set_caption(__file__[47:])

# FPS = 120
# clock = pygame.time.Clock()

screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))

random.randint(0, screen_size[0])

run = True
while run:

    screen.fill(transparent_window.transparency_colour)
    #start

    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)
    pygame.draw.circle(screen, (255, 0, 0), (random.randint(0, screen_size[0]), random.randint(0, screen_size[1])), 100)

    #end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    # clock.tick(FPS)

pygame.quit()
