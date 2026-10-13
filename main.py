
import pygame
from pygame.sprite import Group

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
#            pass
            if event.type == pygame.QUIT:
                return
        _ = screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
#        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000   # regulates the running speed by passing the maximum frame-rate and the program will waiit if needed.

if __name__ == "__main__":
    main()
