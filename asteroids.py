import pygame
from circleshape import * 
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            new_dir_1 = self.velocity.rotate(new_angle)
            new_dir_2 = self.velocity.rotate(0 - new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_astr_1 = Asteroids(self.position.x, self.position.y, new_radius)
            new_astr_2 = Asteroids(self.position.x, self.position.y, new_radius)
            new_astr_1.velocity = new_dir_1 * 1.2
            new_astr_2.velocity = new_dir_2 * 1.2