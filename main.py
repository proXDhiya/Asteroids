from constants import *
import pygame

def init_screen(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init the game, I HAVE NO IDEA WHAT I AM DOING
    init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
