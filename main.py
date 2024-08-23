import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update objects
        for upd in updatable:
            upd.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            collision = asteroid.check_colliding(player)
            if collision:
                print('Game over!')
                sys.exit()

        # Check for shots hitting asteroids
            for shot in shots:
                collision = asteroid.check_colliding(shot)
                if collision:
                    asteroid.split()
                    shot.kill()

        # Draw to screen
        screen.fill((0, 0, 0))

        for drw in drawable:
            drw.draw(screen)

        pygame.display.flip()

        # Limit framerate
        dt = clock.tick(60) / 1000


#     print('Starting asteroids!')
#     print(f'Screen width: {SCREEN_WIDTH}')
#     print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()

