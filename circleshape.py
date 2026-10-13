from typing import override

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]  # pyright: ignore[reportMissingTypeArgument]
    position: pygame.Vector2
    velocity: pygame.Vector2

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType]
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen : pygame.Surface) -> None:
        # must override
        pass

    @override
    def update(self, dt: float) -> None:
        # must override
        pass
