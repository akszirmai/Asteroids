import random
from typing import override

import pygame
from pygame.math import Vector2

import circleshape
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(circleshape.CircleShape):
    position : pygame.Vector2

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        center = Vector2(self.position.x, self.position.y)
        _ = pygame.draw.circle(screen, "red", center, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
#        print("Asteroid killed")
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle: float = random.uniform(20, 50)
        velo_vect_1 : Vector2 = self.velocity.rotate(angle)
        velo_vect_2 : Vector2 = self.velocity.rotate(-angle)
        new_radius : float = self.radius - ASTEROID_MIN_RADIUS
#        print(f"Astro1 created at: ({self.position.x}, {self.position.y}), with speed vector: [{velo_vect_1.x}, {velo_vect_1.y}] and radius: {new_radius}")
        astro1 = Asteroid(self.position.x, self.position.y, new_radius)
        astro1.velocity = velo_vect_1 * 1.2
        astro2 = Asteroid(self.position.x, self.position.y, new_radius)
        astro2.velocity = velo_vect_2 * 1.2
