import pygame
import numpy as np
from Main.C_planet import Planet

pygame.init()
window = pygame.display.set_mode((1280,720))
window_midpoint = (640, 360)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    # Draw star + planets
    pygame.draw.circle(window, (255,234,0), window_midpoint, 35) # Star
    mercury = Planet("Mercury", 5, (158,158,158), 100)
    venus = Planet("Venus", 10, (217,108,0), 150)
    earth = Planet("Earth", 15, (0,0,255), 225)
    mercury.draw(window, window_midpoint, pygame.time.get_ticks()*0.001)
    venus.draw(window, window_midpoint, pygame.time.get_ticks()*0.001)
    earth.draw(window, window_midpoint, pygame.time.get_ticks()*0.001)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()