import pygame
from player import Player
from constants import *

def setup_pygame(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    return screen, clock

def setup_groups(player):
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (drawable, updatable)

    drawable.add(player)
    updatable.add(player)

    return drawable, updatable

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update_screen(screen, drawable, updatable, dt):
    screen.fill("black")

    for entity in drawable:
        entity.draw(screen)

    for entity in updatable:
        entity.update(dt)

    pygame.display.flip()

def init_screen(width, height):
    screen, clock = setup_pygame(width, height)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    drawable, updatable = setup_groups(player)

    dt = 0
    running = True

    while running:
        running = handle_events()
        update_screen(screen, drawable, updatable, dt)
        dt = clock.tick(60) / 1000

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
