import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update objects
        for upd in updatable:
            upd.update(dt)

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

