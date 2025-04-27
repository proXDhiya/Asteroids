# My First Game Submission: Asteroids

Hi! This is my first game built with Python and Pygame, submitted as part of the [boot.dev](https://www.boot.dev/courses/build-asteroids-python) backend learning challenge. Since this is my first time writing Python and making a game, I kept things simple and focused on learning the basics.

Here’s a walkthrough of my project, how it works, and what I learned along the way.

---

## What Is This Game?

I made a classic arcade-style game called **Asteroids**. You control a spaceship that can spin, move, and shoot bullets to break apart asteroids flying in from the edges of the screen.

The asteroids split into smaller pieces when hit, and the goal is to survive as long as possible without crashing.

![Gameplay demo](./assets/game-play.gif)

---

## How I Organized My Project

I wanted to keep my code clean and easy to understand, so I split it into folders and files based on their roles:

```
/project_root
│
├── main.py                  # Starts the game
├── constants.py             # Game settings like screen size and speeds
├── requirements.txt         # Lists Python packages needed to run the game
│
├── core/                    # Main game loop and asteroid spawning
│   ├── game.py              # Runs the game and handles input
│   └── asteroidfield.py     # Creates and manages asteroids
│
├── entities/                # Game objects like player, asteroids, shots
│   ├── circleshape.py       # Base class for round objects
│   ├── player.py            # Player spaceship code
│   ├── asteroid.py          # Asteroid behavior
│   └── shot.py              # Bullets fired by the player
```

---

## How the Game Works — Simple Breakdown

### Starting the Game (main.py)

This file just prints some info and calls the main game loop:

```python
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from core.game import init_screen

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    init_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
```

---

### Game Settings (constants.py)

All the important numbers are here, like how big the screen is, how fast the player moves, and how often asteroids spawn.

```python
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

SHOT_RADIUS = 5
```

---

### The Game Loop (core/game.py)

This is where the magic happens:

- It sets up the screen and clock.
- Creates groups for drawing and updating sprites.
- Handles keyboard input.
- Updates and draws everything each frame.
- Checks for collisions between player, asteroids, and shots.

Example of handling quit events:

```python
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
```

---

### Asteroid Spawning (core/asteroidfield.py)

Asteroids spawn randomly from the edges of the screen at random speeds and directions. The spawning is controlled by a timer so they don’t come too fast.

---

### Game Objects (entities/ folder)

I created a base class `CircleShape` for all round objects (player, asteroids, shots) to share common properties like position, velocity, and collision detection.

Example collision check:

```python
def collisions_detected(self, circle):
    distance = self.position.distance_to(circle.position)
    return distance <= (self.radius + circle.radius)
```

---

### Player (entities/player.py)

The player can:

- Rotate left/right with `A` and `D`.
- Move forward/backward with `W` and `S`.
- Shoot bullets with `SPACE` (with a cooldown).

Here’s how the ship is drawn as a triangle pointing in the direction it’s facing:

```python
def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)
```

---

### Asteroids (entities/asteroid.py)

Asteroids move and split into smaller asteroids when hit by a shot, unless they’re already at the smallest size.

Splitting example:

```python
def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
        return
    random_angle = random.uniform(20, 50)
    velocity1 = self.velocity.rotate(random_angle) * 1.2
    velocity2 = self.velocity.rotate(-random_angle) * 1.2
    new_radius = self.radius - ASTEROID_MIN_RADIUS

    a1 = Asteroid(self.position.x, self.position.y, new_radius)
    a1.velocity = velocity1

    a2 = Asteroid(self.position.x, self.position.y, new_radius)
    a2.velocity = velocity2
```

---

### Shots (entities/shot.py)

Shots are small circles that fly straight in the direction the player was facing when fired.

---

## How to Play

- Press **A** and **D** to spin your ship.
- Press **W** and **S** to move forward and backward.
- Press **SPACE** to shoot.
- Avoid crashing into asteroids.
- Shoot asteroids to break them up and survive longer.

---

## Setup and Run the Game

1. **Create a Virtual Environment:**

   If you don't have a virtual environment set up, create one with the following command:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment:**

   - On **Windows**, use:

     ```bash
     venv\Scripts\activate
     ```

   - On **Mac/Linux**, use:

     ```bash
     source venv/bin/activate
     ```

3. **Install the Required Packages:**

   Install the required Python packages listed in `requirements.txt`:

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run the Game:**

   Now you can start the game by running:

   ```bash
   python3 main.py
   ```
 
---

## Some Space Humor to Keep You Going

- Why don’t asteroids ever get invited to parties?  
  Because they always cause a big crash! 💥

- If your ship feels slow, try tweaking `PLAYER_SPEED` in `constants.py`. Just don’t go so fast you fly off into a black hole!

- Remember, no laser spamming — shots have a cooldown!

---

## What I Learned and What’s Next

This project helped me:

- Understand Python basics and syntax.
- Learn how to use Pygame for graphics and input.
- Practice organizing code with folders and classes.
- Use vectors for movement and collision detection.
- Build a simple but fun game loop.

Next, I want to try:

- Adding a score counter.
- Making a start menu and game over screen.
- Adding sound effects.
- Improving asteroid behavior.

---

## Final Thoughts

Building this game was a fun challenge and a great way to learn Python and game programming basics. I’m excited to keep improving it and learning more!

Thanks for checking out my submission. If you have feedback or tips, I’m all ears!

---

Happy coding and may your shots always hit their mark! 🎯🚀