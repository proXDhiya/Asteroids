from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from core.game import init_screen

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
