import pygame
from constants import SHOT_RADIUS
from entities.circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt
