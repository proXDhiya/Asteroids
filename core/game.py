import pygame
import sys
from core.asteroidfield import AsteroidField
from entities.asteroid import Asteroid
from entities.player import Player
from entities.shot import Shot

def setup_pygame(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    return screen, clock

def setup_groups(player, shots):
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    drawable.add(player)
    updatable.add(player)

    return drawable, updatable, asteroids

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update_screen(screen, drawable, updatable, dt, player, asteroids, shots):
    screen.fill("black")

    for entity in drawable:
        entity.draw(screen)

    for entity in updatable:
        entity.update(dt)

    for asteroid in asteroids:
        if player.collisions_detected(asteroid):
            print("Game over!")
            sys.exit()
        for shot in shots:
            if asteroid.collisions_detected(shot):
                asteroid.split()
                shot.kill()

    pygame.display.flip()

def init_screen(width, height):
    screen, clock = setup_pygame(width, height)
    shots = pygame.sprite.Group()
    player = Player(width / 2, height / 2, shots)
    drawable, updatable, asteroids = setup_groups(player, shots)
    asteroid_field = AsteroidField()

    dt = 0
    running = True

    while running:
        running = handle_events()
        update_screen(screen, drawable, updatable, dt, player, asteroids, shots)
        dt = clock.tick(60) / 1000
