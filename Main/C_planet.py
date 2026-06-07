import numpy as np
import pygame

class Planet:
    def __init__(self, name, radius, colour, distance_from_star):
        self.name = name
        self.radius = radius
        self.colour = colour
        self.distance_from_star = distance_from_star

    def draw(self, window, star_position, time):
        x = star_position[0] + int(self.distance_from_star * np.cos(time))
        y = star_position[1] + int(self.distance_from_star * np.sin(time))
        pygame.draw.circle(window, self.colour, (x,y), self.radius)