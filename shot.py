from typing import override

import pygame
from pygame.math import Vector2

import circleshape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(circleshape.CircleShape):
    position : pygame.Vector2

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    @override
    def draw(self, screen : pygame.Surface) -> None:
        center = Vector2(self.position.x, self.position.y)
        _ = pygame.draw.circle(screen, "green", center, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
