# PyGame Workbook — Building a Game, Building NEA Skills

*OCR A Level Computer Science (H446) — Component 03/04 (Programming Project) preparation, practising Component 02 (2.2 Programming techniques) in a real library.*

## How to use this workbook

This workbook is a set of graded **practical coding challenges** using the **pygame** library. It runs across four homework/consolidation sessions (SOW weeks 22, 25, 26 and 28). By the end you will have built a complete small game — and, more importantly, practised every *development skill* the NEA mark scheme rewards: modular code, classes, file handling, validation, iterative testing and refinement.

For each challenge:

1. **Read the goal and the hints.**
2. **Attempt it yourself** in a code editor before opening the solution. Run it. Break it. Fix it.
3. **Only then** expand the `Solution` box and compare. If your code differs but works, that is fine — there is rarely one correct answer.
4. If you got stuck, type the solution out yourself rather than copy-pasting, then **change something** — a speed, a colour, a rule — and predict what will happen before you run it.

Solutions are written in **Python 3** with **pygame 2.x**. Every solution is a complete, runnable program.

**Difficulty tags:**

- ★ **Foundation** — core pygame patterns you must be fluent in.
- ★★ **Developing** — combining techniques; the level your NEA code should sit at.
- ★★★ **Stretch** — closer to a finished, polished game.

**Why pygame for the NEA?** You do *not* have to use pygame for your project — but a game (or simulation, or visualisation) built with it ticks the boxes the NEA marking criteria look for: a real event loop, object-oriented sprites, collision algorithms, file persistence and a testable, demonstrable product. Each challenge carries an **NEA link** callout showing which piece of *Development & Testing* evidence the skill maps to.

**Session map**

| Session | SOW week | Challenges | Focus |
|---------|----------|------------|-------|
| 1 | Week 22 | 1–8 | Install, window, game loop, events, drawing, keyboard movement |
| 2 | Week 25 | 9–16 | Sprite classes, images, collision detection, score display |
| 3 | Week 26 | 17–24 | Sound, sprite groups, enemy behaviour, game states |
| 4 | Week 28 | 25–30 | High-score file persistence, polish, extension mini-projects |

---

## Session 1 (Week 22) — Window, Loop, Events, Movement

The heart of every game is the **game loop**: handle events → update the game state → draw the frame → repeat, dozens of times per second. This session gets that loop under your fingers.

### Challenge 1 — Install and verify pygame ★

**Goal:** Install pygame and prove it works by printing its version number and initialising it.

**Hints**

- Install from a terminal/command prompt with `python -m pip install pygame` (on school networks you may need `python -m pip install --user pygame`).
- `pygame.version.ver` holds the version string; `pygame.init()` starts up all pygame modules.

**Example**

```
pygame version: 2.6.1
pygame initialised: 6 modules OK, 0 failed
```

<details><summary>Solution</summary>

```python
import pygame

print("pygame version:", pygame.version.ver)

ok, failed = pygame.init()
print("pygame initialised:", ok, "modules OK,", failed, "failed")

pygame.quit()
```

`pygame.init()` returns a tuple `(number_succeeded, number_failed)`. If the import itself fails, pygame is not installed for the Python you are running — check with `python --version` that you are using the same interpreter you installed into.

</details>

> 💡 **NEA link:** your Analysis section should state the language *and libraries* your solution needs, and your Development evidence should show the environment working. A screenshot of this exact check is legitimate first-iteration evidence.

### Challenge 2 — Open a game window ★

**Goal:** Open an 800 × 600 window titled `My First Game` that stays open until the user clicks its close button, then shuts down cleanly.

**Hints**

- `pygame.display.set_mode((width, height))` creates the window and returns the drawing surface.
- The window will freeze ("Not responding") unless you keep *pumping events*: loop over `pygame.event.get()` every frame.
- The close button generates an event of type `pygame.QUIT`.

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

The `while running` loop is the skeleton of every pygame program. We never `break` out from deep inside the loop; we set the flag `running = False` and let the loop finish the frame — a tidy, single exit point.

</details>

> 💡 **NEA link:** "the program opens and closes without crashing" is a genuine (if basic) success criterion — and this event-pumping pattern is the fix for the classic *frozen window* defect worth documenting in your testing log.

### Challenge 3 — The full game loop ★

**Goal:** Extend Challenge 2 into the standard three-phase game loop — **handle events, update, draw** — with a dark blue background, redrawn at a fixed 60 frames per second.

**Hints**

- `screen.fill((r, g, b))` paints the whole surface one colour; colours are tuples of 0–255 values.
- Nothing appears until you call `pygame.display.flip()` — drawing happens on a hidden buffer first (*double buffering*).
- Create a `pygame.time.Clock()` before the loop and call `clock.tick(60)` at the end of every frame to cap the frame rate.

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Game Loop")
clock = pygame.time.Clock()

running = True
while running:
    # 1. handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. update the game state (nothing to update yet)

    # 3. draw the frame
    screen.fill((30, 30, 60))
    pygame.display.flip()

    clock.tick(60)   # wait so the loop runs at most 60 times per second

pygame.quit()
```

Without `clock.tick(60)` the loop would spin as fast as the CPU allows, using 100% of a core and running at different speeds on different machines. Capping the frame rate makes movement speeds predictable.

</details>

> 💡 **NEA link:** the loop's three numbered phases are a ready-made **decomposition** — exactly the structure-chart breakdown your Design section needs (input handling / game logic / rendering).

### Challenge 4 — Reacting to events ★

**Goal:** Make the background turn red **while** the space bar is held down, and print the mouse coordinates to the console whenever the window is clicked.

**Hints**

- Keyboard events are `pygame.KEYDOWN` and `pygame.KEYUP`; the key involved is in `event.key` and space is `pygame.K_SPACE`.
- Mouse clicks are `pygame.MOUSEBUTTONDOWN`; the position clicked is in `event.pos`.

**Example (console output)**

```
Mouse clicked at (412, 187)
Mouse clicked at (95, 540)
```

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Event Detective")
clock = pygame.time.Clock()

background = (30, 30, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                background = (200, 60, 60)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                background = (30, 30, 60)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse clicked at", event.pos)

    screen.fill(background)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Events are pygame's version of **event-driven programming**: the operating system queues up everything the user does, and your loop drains that queue once per frame. `KEYDOWN` fires once when the key goes down; the colour stays red because we only change it back on `KEYUP`.

</details>

> 💡 **NEA link:** logging events with `print()` like this is a simple but effective **debugging/trace technique** — screenshot the console alongside the window as evidence of how you verified input handling.

### Challenge 5 — Drawing shapes ★

**Goal:** Draw a simple scene: a green rectangle "ground" across the bottom, a yellow circle "sun", a red square "house" sitting on the ground, and a white diagonal line "path".

**Hints**

- `pygame.draw.rect(screen, colour, pygame.Rect(x, y, width, height))`
- `pygame.draw.circle(screen, colour, (centre_x, centre_y), radius)`
- `pygame.draw.line(screen, colour, (x1, y1), (x2, y2), thickness)`
- Remember the pygame coordinate system: **(0, 0) is the top-left** and y increases *downwards*.

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shape Scene")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((120, 180, 240))                                    # sky
    pygame.draw.rect(screen, (60, 160, 60), pygame.Rect(0, 500, 800, 100))   # ground
    pygame.draw.circle(screen, (250, 220, 60), (700, 90), 50)               # sun
    pygame.draw.rect(screen, (200, 60, 60), pygame.Rect(150, 400, 100, 100)) # house
    pygame.draw.line(screen, (255, 255, 255), (200, 500), (500, 590), 5)     # path
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Everything is redrawn from scratch every frame — that is normal. Draw order matters: later calls paint *over* earlier ones, so the background is filled first and details go on top.

</details>

> 💡 **NEA link:** a labelled screenshot of a drawn scene next to the **UI wireframe from your Design section** is exactly the "design → implementation" pairing that scores in Development.

### Challenge 6 — A moving square ★★

**Goal:** Animate a square moving smoothly from the left edge to the right edge of the window. When it disappears off the right-hand side, it should reappear on the left.

**Hints**

- Store the square's position in a variable and add a small amount to it every frame (that is the whole secret of animation).
- Update the position in phase 2 of the loop, then draw at the new position in phase 3.
- "Wrap around": when `x` is past the right edge, reset it to just off the left edge.

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Runaway Square")
clock = pygame.time.Clock()

x = -50            # start just off the left edge
y = 275
speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    x = x + speed
    if x > 800:            # fully off the right edge
        x = -50            # wrap to just off the left

    # draw
    screen.fill((30, 30, 60))
    pygame.draw.rect(screen, (80, 200, 120), pygame.Rect(x, y, 50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

At 60 frames per second and 4 pixels per frame, the square crosses the 800-pixel window in about 3.5 seconds. Change `speed` and `clock.tick()` and observe the relationship — movement per second = pixels per frame × frames per second.

</details>

> 💡 **NEA link:** predicting the crossing time and then timing it is a **test with expected vs actual results** — the exact format your NEA test tables need.

### Challenge 7 — Bouncing ball ★★

**Goal:** Make a ball bounce around the window, reversing direction whenever it hits any edge.

**Hints**

- You need *two* velocity variables, `dx` and `dy`, added to the position each frame.
- To bounce, negate the relevant velocity: `dx = -dx` when a side wall is hit, `dy = -dy` for top/bottom.
- Test the edge conditions carefully with the ball's **radius**, or the ball will sink half-way into the wall before bouncing — a classic boundary error.

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

x, y = 400, 300
dx, dy = 5, 3
radius = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    x = x + dx
    y = y + dy
    if x - radius < 0 or x + radius > 800:
        dx = -dx
    if y - radius < 0 or y + radius > 600:
        dy = -dy

    # draw
    screen.fill((30, 30, 60))
    pygame.draw.circle(screen, (240, 120, 60), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

The boundary tests use `x - radius` and `x + radius` (the ball's edges), not `x` (its centre). Try changing them to plain `x` and watch the ball half-bury itself in the wall — then you have *seen* a boundary error, not just read about one.

</details>

> 💡 **NEA link:** boundary conditions are where marks are won: your test plan must include **normal, boundary and erroneous** data. "Ball at exactly x = radius" is a textbook boundary case to evidence.

### Challenge 8 — Move a sprite with the keys ★★

**Goal:** Draw a player square that the user steers with the **arrow keys** in all four directions (including diagonals), and that can never leave the window.

**Hints**

- For held-down movement keys, don't use `KEYDOWN` events — read the live keyboard state with `keys = pygame.key.get_pressed()` and test `keys[pygame.K_LEFT]`, `keys[pygame.K_RIGHT]`, `keys[pygame.K_UP]`, `keys[pygame.K_DOWN]`.
- Use a `pygame.Rect` for the player: it stores x, y, width and height together and has a handy `clamp_ip()` method to keep one rect inside another.

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Arrow Key Hero")
clock = pygame.time.Clock()

player = pygame.Rect(375, 275, 50, 50)
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update — read which keys are held right now
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x = player.x - speed
    if keys[pygame.K_RIGHT]:
        player.x = player.x + speed
    if keys[pygame.K_UP]:
        player.y = player.y - speed
    if keys[pygame.K_DOWN]:
        player.y = player.y + speed
    player.clamp_ip(screen.get_rect())   # keep the player on screen

    # draw
    screen.fill((30, 30, 60))
    pygame.draw.rect(screen, (80, 200, 120), player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Four separate `if` statements (not `elif`) allow diagonal movement because two can be true at once. `clamp_ip()` moves the player rect *in place* so it always stays inside the screen rect — one line of validation instead of four edge checks.

</details>

> 💡 **NEA link:** input handling + validation ("player cannot leave the play area") is your first piece of **robustness** evidence — the marking criteria explicitly reward solutions that cannot be broken by user input.

---

## Session 2 (Week 25) — Sprite Classes, Images, Collision, Score

Real games are built from **objects**. This session converts the loose variables of Session 1 into proper classes using `pygame.sprite.Sprite`, loads image files, detects collisions and displays a score — the core of almost every NEA game.

### Challenge 9 — A Player class ★★

**Goal:** Rewrite Challenge 8 with the player as a **class** that inherits from `pygame.sprite.Sprite`, with its movement code inside an `update()` method.

**Hints**

- A pygame sprite needs two attributes: `self.image` (a `pygame.Surface` to draw) and `self.rect` (where to draw it).
- Call `super().__init__()` first in your constructor.
- `pygame.Surface((w, h))` makes a blank image; `.fill(colour)` colours it; `image.get_rect(center=(x, y))` gives a matching rect.

<details><summary>Solution</summary>

```python
import pygame

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Class")
clock = pygame.time.Clock()

player = Player(WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    screen.fill((30, 30, 60))
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Nothing new *happens* on screen — that is the point. This is a **refactor**: same behaviour, better structure. `Player` now owns its own image, position and movement rules (**encapsulation**), so the main loop shrinks to `player.update()`.

</details>

> 💡 **NEA link:** refactoring working code into classes *is* an iteration. Evidence it as one: "Iteration 2 — restructured player into a class; re-ran movement tests 1–4 to confirm no regression." Regression testing is top-band behaviour.

### Challenge 10 — Sprite groups ★★

**Goal:** Create a `Block` sprite class and put **eight** blocks, at random positions with random horizontal speeds, into a `pygame.sprite.Group`. Blocks bounce off the left/right edges. Update and draw them all with two lines in the main loop.

**Hints**

- `blocks = pygame.sprite.Group()` then `blocks.add(sprite)`.
- `blocks.update()` calls `update()` on every sprite in the group; `blocks.draw(screen)` blits every sprite's `image` at its `rect`.
- Use `random.randint()` for positions and `random.choice([-4, -3, 3, 4])` so no block gets speed 0.

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((240, 120, 60))
        x = random.randint(0, WIDTH - 40)
        y = random.randint(0, HEIGHT - 40)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dx = random.choice([-4, -3, 3, 4])

    def update(self):
        self.rect.x = self.rect.x + self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Groups")
clock = pygame.time.Clock()

blocks = pygame.sprite.Group()
for i in range(8):
    blocks.add(Block())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    blocks.update()          # one line updates all eight

    screen.fill((30, 30, 60))
    blocks.draw(screen)      # one line draws all eight
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

A `Group` is a container that knows how to update and draw everything inside it. Eight blocks or eight hundred — the main loop stays two lines. This is **polymorphism in practice**: the group calls `update()` on each sprite without caring what class it is.

</details>

> 💡 **NEA link:** in your Design section, justify groups as your chosen **data structure** for managing many game objects ("a group supports add/remove/iterate, which the game needs when enemies spawn and die").

### Challenge 11 — Loading an image ★★

**Goal:** Give the `Player` class a real image loaded from a file `player.png`, scaled to 50 × 50. If the file is missing, the program must **not crash** — fall back to the plain coloured square.

**Hints**

- `pygame.image.load("player.png").convert_alpha()` loads a PNG and keeps its transparency; call it *after* `set_mode()`.
- `pygame.transform.scale(image, (50, 50))` resizes.
- Wrap the load in `try:` / `except (pygame.error, FileNotFoundError):` and build a `pygame.Surface` fallback in the `except` branch.
- Any 50 × 50-ish PNG works — draw one in any paint program or export one from an asset site your school allows (record the source!).

<details><summary>Solution</summary>

```python
import pygame

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            image = pygame.image.load("player.png").convert_alpha()
            self.image = pygame.transform.scale(image, (50, 50))
        except (pygame.error, FileNotFoundError):
            # graceful fallback: a plain square instead of a crash
            self.image = pygame.Surface((50, 50))
            self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Sprite")
clock = pygame.time.Clock()

player = Player(WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    screen.fill((30, 30, 60))
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

The image path is relative to where you *run* the program from, so keep assets next to the `.py` file. The `try`/`except` is genuine **exception handling** — the program degrades gracefully rather than dying with a traceback.

</details>

> 💡 **NEA link:** two lessons for your write-up: (1) exception handling around every file access is core robustness evidence; (2) any asset you did not make yourself must be **acknowledged with its source** in your report.

### Challenge 12 — A field of coins ★★

**Goal:** Create a `Coin` sprite class (a small yellow circle on a transparent background) and scatter **ten** coins at random positions across the screen using a group. The player from Challenge 9 walks around them (no collection yet).

**Hints**

- For a circular image: create the surface with `pygame.Surface((20, 20), pygame.SRCALPHA)` (transparent), then `pygame.draw.circle` onto it.
- Random positions: keep coins fully on screen — the coordinate range must allow for the coin's size (a boundary detail!).

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)   # transparent
        pygame.draw.circle(self.image, (250, 210, 60), (10, 10), 10)
        x = random.randint(10, WIDTH - 10)
        y = random.randint(10, HEIGHT - 10)
        self.rect = self.image.get_rect(center=(x, y))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Field")
clock = pygame.time.Clock()

player = Player(WIDTH // 2, HEIGHT // 2)
coins = pygame.sprite.Group()
for i in range(10):
    coins.add(Coin())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    screen.fill((30, 30, 60))
    coins.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

`pygame.SRCALPHA` gives the surface a transparency channel, so the corners around the circle are see-through instead of black. Note the random ranges `10` to `WIDTH - 10`: with a 20-pixel coin centred at that coordinate, no coin can poke off screen.

</details>

> 💡 **NEA link:** the coin-placement range is a designed-in boundary decision. Writing "coins are constrained to fully visible positions because…" in your Design, then testing the extreme positions, shows **design → implementation → test** traceability.

### Challenge 13 — Collision with `colliderect` ★★

**Goal:** Draw a fixed "danger zone" rectangle in the middle of the screen. While the arrow-key player overlaps it, the zone turns bright red and `WARNING` is printed once per entry (not once per frame!).

**Hints**

- `rect_a.colliderect(rect_b)` returns `True` if two rects overlap — this is pygame's basic collision test.
- To print only on *entering* the zone, remember last frame's state in a Boolean and act only when the state changes from `False` to `True`.

<details><summary>Solution</summary>

```python
import pygame

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Danger Zone")
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 50, 50)
danger = pygame.Rect(300, 200, 200, 200)
speed = 5
was_inside = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x = player.x - speed
    if keys[pygame.K_RIGHT]:
        player.x = player.x + speed
    if keys[pygame.K_UP]:
        player.y = player.y - speed
    if keys[pygame.K_DOWN]:
        player.y = player.y + speed
    player.clamp_ip(screen.get_rect())

    inside = player.colliderect(danger)
    if inside and not was_inside:
        print("WARNING")          # fires once, on the frame we enter
    was_inside = inside

    screen.fill((30, 30, 60))
    if inside:
        pygame.draw.rect(screen, (220, 40, 40), danger)
    else:
        pygame.draw.rect(screen, (120, 60, 60), danger)
    pygame.draw.rect(screen, (80, 200, 120), player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Rect-overlap is the collision algorithm behind most 2D games. The `was_inside` flag is **edge detection**: turning a continuous condition ("is overlapping") into a one-off event ("has just started overlapping") — you will reuse this trick constantly.

</details>

> 💡 **NEA link:** describe `colliderect` (or your own overlap test) as an **algorithm** in Design — a labelled diagram of two overlapping rectangles and the four comparison conditions makes strong algorithmic-design evidence.

### Challenge 14 — Collecting coins with `spritecollide` ★★

**Goal:** Combine Challenges 12 and 13: when the player touches a coin, the coin disappears. Print the running total collected.

**Hints**

- `pygame.sprite.spritecollide(sprite, group, dokill)` returns a **list** of sprites in `group` that collide with `sprite`; with `dokill=True` they are also removed from the group automatically.
- The length of the returned list tells you how many were collected this frame.

**Example (console output)**

```
Collected 1 coin(s), total 1
Collected 1 coin(s), total 2
Collected 2 coin(s), total 4
```

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (250, 210, 60), (10, 10), 10)
        x = random.randint(10, WIDTH - 10)
        y = random.randint(10, HEIGHT - 10)
        self.rect = self.image.get_rect(center=(x, y))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")
clock = pygame.time.Clock()

player = Player(WIDTH // 2, HEIGHT // 2)
coins = pygame.sprite.Group()
for i in range(10):
    coins.add(Coin())
total = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    grabbed = pygame.sprite.spritecollide(player, coins, True)
    if len(grabbed) > 0:
        total = total + len(grabbed)
        print("Collected", len(grabbed), "coin(s), total", total)

    screen.fill((30, 30, 60))
    coins.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

`spritecollide` loops over the group doing a `colliderect` against each member — the library version of the algorithm you met in Challenge 13, applied across a whole data structure. `dokill=True` removes collected coins from the group so they stop being drawn.

</details>

> 💡 **NEA link:** when you use a library routine like `spritecollide`, *say what it does algorithmically* in your write-up (linear pass, rect-overlap test per element). Understanding, not just calling, is what the moderator looks for.

### Challenge 15 — Displaying the score ★★

**Goal:** Replace Challenge 14's console printing with a proper on-screen score, drawn in the top-left corner in white text and updating live.

**Hints**

- Create a font once, before the loop: `font = pygame.font.SysFont(None, 36)` (`None` = pygame's default font).
- Text must be rendered to a surface each frame: `text_surface = font.render("Score: " + str(score), True, (255, 255, 255))`, then `screen.blit(text_surface, (10, 10))`.
- The second argument to `render` turns on anti-aliasing (smooth edges).

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (250, 210, 60), (10, 10), 10)
        x = random.randint(10, WIDTH - 10)
        y = random.randint(10, HEIGHT - 10)
        self.rect = self.image.get_rect(center=(x, y))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Score Display")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = Player(WIDTH // 2, HEIGHT // 2)
coins = pygame.sprite.Group()
for i in range(10):
    coins.add(Coin())
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    grabbed = pygame.sprite.spritecollide(player, coins, True)
    score = score + len(grabbed) * 10

    screen.fill((30, 30, 60))
    coins.draw(screen)
    screen.blit(player.image, player.rect)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Text in pygame is just another surface — render it, blit it, every frame. Creating the *font* is relatively slow, so that is done once before the loop; rendering the *text* is cheap and happens per frame because the score changes.

</details>

> 💡 **NEA link:** live feedback to the user (score, lives, status) is a **usability feature** — the kind you should list in your Design section as meeting a specific stakeholder need, then evidence with a screenshot.

### Challenge 16 — Mini-game: Coin Chaser v1 ★★★

**Goal:** Assemble the session into one complete mini-game. Ten coins; arrow-key player; +10 points each coin; when the last coin is collected, display `You win! Final score: 100` in the centre of the screen (the game keeps running so the message stays visible).

**Hints**

- You have written every piece already — this challenge is about **integration**.
- A group knows its own size: `len(coins) == 0` means the field is empty.
- To centre text: render it, then `text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))` and blit at `text_rect`.

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (250, 210, 60), (10, 10), 10)
        x = random.randint(10, WIDTH - 10)
        y = random.randint(10, HEIGHT - 10)
        self.rect = self.image.get_rect(center=(x, y))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Chaser v1")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)

player = Player(WIDTH // 2, HEIGHT // 2)
coins = pygame.sprite.Group()
for i in range(10):
    coins.add(Coin())
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    grabbed = pygame.sprite.spritecollide(player, coins, True)
    score = score + len(grabbed) * 10

    screen.fill((30, 30, 60))
    coins.draw(screen)
    screen.blit(player.image, player.rect)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if len(coins) == 0:
        win_text = big_font.render("You win! Final score: " + str(score), True,
                                   (250, 210, 60))
        win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(win_text, win_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Notice how little *new* code this needed — good decomposition earlier makes integration almost free. Test it like an examiner: can the score ever exceed 100? Can a coin spawn under the player and be collected instantly? Is that a bug or a feature? Decide, and write the rule down.

</details>

> 💡 **NEA link:** this is a complete **iteration**: a working, testable build. Photograph/screenshot it, run your test table against it, note the defects and the fixes. That develop → test → review → refine cycle, repeated, is the single biggest source of Development marks.

---

## Session 3 (Week 26) — Sound, Enemies, Game States

A game becomes a *game* when something pushes back. This session adds audio feedback, enemies with their own behaviour, timed spawning, and a proper title → playing → game-over structure.

### Challenge 17 — Sound effects ★★

**Goal:** Play a collect sound (`coin.wav`) whenever the player picks up a coin in Coin Chaser. The game must still run correctly if the sound file is missing or the machine has no audio.

**Hints**

- Load once, before the loop: `collect_sound = pygame.mixer.Sound("coin.wav")`; play with `collect_sound.play()`.
- Wrap the load in `try:` / `except (pygame.error, FileNotFoundError):` and set the variable to `None` on failure; only call `.play()` if it is not `None`.
- Any short `.wav` or `.ogg` works — free sound sites are fine if your school allows them (record the source).

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (250, 210, 60), (10, 10), 10)
        x = random.randint(10, WIDTH - 10)
        y = random.randint(10, HEIGHT - 10)
        self.rect = self.image.get_rect(center=(x, y))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Chaser + Sound")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

try:
    collect_sound = pygame.mixer.Sound("coin.wav")
except (pygame.error, FileNotFoundError):
    collect_sound = None      # no sound available — carry on silently

player = Player(WIDTH // 2, HEIGHT // 2)
coins = pygame.sprite.Group()
for i in range(10):
    coins.add(Coin())
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    grabbed = pygame.sprite.spritecollide(player, coins, True)
    if len(grabbed) > 0:
        score = score + len(grabbed) * 10
        if collect_sound is not None:
            collect_sound.play()

    screen.fill((30, 30, 60))
    coins.draw(screen)
    screen.blit(player.image, player.rect)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

`pygame.mixer` handles audio; short effects are `Sound` objects loaded once and played on demand. The `None` fallback means the game's *core* function never depends on an optional asset — a deliberate robustness decision.

</details>

> 💡 **NEA link:** "runs correctly with assets missing" is a superb erroneous-case test. Delete the `.wav`, screenshot the game still working, and put it in your test evidence.

### Challenge 18 — Background music ★

**Goal:** Loop a background music track (`music.ogg`) for as long as the game runs, at half volume — again without crashing if the file is absent.

**Hints**

- Music uses a different API from sound effects (it *streams* rather than loading fully): `pygame.mixer.music.load("music.ogg")`, `pygame.mixer.music.set_volume(0.5)`, `pygame.mixer.music.play(-1)`.
- The argument `-1` means "loop forever".

<details><summary>Solution</summary>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Background Music")
clock = pygame.time.Clock()

try:
    pygame.mixer.music.load("music.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)     # -1 = loop forever
except (pygame.error, FileNotFoundError):
    print("No music file found — continuing without music")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 60))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

`Sound` objects are for short effects that may overlap (several coin pings at once); `mixer.music` streams one long track from disk. Knowing *why* a library offers two APIs — memory versus streaming — is exactly the sort of understanding worth a sentence in your write-up.

</details>

> 💡 **NEA link:** stakeholder feedback often mentions audio ("it felt dead without sound"). Capturing that feedback and responding to it in a later iteration is Evaluation-linked Development evidence.

### Challenge 19 — A patrolling enemy ★★

**Goal:** Create an `Enemy` sprite that patrols left and right across the screen on its own, reversing at the edges — no user input involved.

**Hints**

- This is the bouncing logic from Challenge 10 given a class of its own and a menacing colour.
- Give the constructor `x`, `y` and `speed` parameters so you can place different enemies later.

<details><summary>Solution</summary>

```python
import pygame

WIDTH, HEIGHT = 800, 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = speed

    def update(self):
        self.rect.x = self.rect.x + self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx      # patrol: reverse at the edges

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Patrolling Enemy")
clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
enemies.add(Enemy(200, 150, 3))
enemies.add(Enemy(600, 300, -4))
enemies.add(Enemy(400, 450, 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    enemies.update()

    screen.fill((30, 30, 60))
    enemies.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Each enemy carries its own `dx`, so the three patrol independently even though they share one `update()` method — the whole point of instance attributes. Parameterising `speed` (including negatives for leftward starts) makes the class reusable.

</details>

> 💡 **NEA link:** autonomous behaviour driven by rules is **algorithmic content** — the thing that separates top-band projects from CRUD forms. Document the patrol rule as a state diagram or pseudocode in Design.

### Challenge 20 — A chasing enemy ★★★

**Goal:** Make a second enemy type, `Chaser`, that moves *towards the player* every frame — slightly slower than the player, so a skilful player can escape.

**Hints**

- Simplest chase algorithm: each frame, compare positions. If the player's centre x is greater than the chaser's, move right, otherwise left; same for y.
- The chaser needs to *know about* the player — pass the player object into `update()`.
- Make the chaser's speed 3 against the player's 5, or it becomes unavoidable (playtesting = testing!).

<details><summary>Solution</summary>

```python
import pygame

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Chaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3          # slower than the player — escapable

    def update(self, player):
        if self.rect.centerx < player.rect.centerx:
            self.rect.x = self.rect.x + self.speed
        elif self.rect.centerx > player.rect.centerx:
            self.rect.x = self.rect.x - self.speed
        if self.rect.centery < player.rect.centery:
            self.rect.y = self.rect.y + self.speed
        elif self.rect.centery > player.rect.centery:
            self.rect.y = self.rect.y - self.speed

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaser")
clock = pygame.time.Clock()

player = Player(WIDTH // 2, HEIGHT // 2)
chaser = Chaser(50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    chaser.update(player)

    screen.fill((30, 30, 60))
    screen.blit(chaser.image, chaser.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

This sign-comparison chase is deliberately simple (the chaser moves diagonally at slightly higher effective speed — can you see why?). A stretch refinement is a *normalised vector* chase: compute `dx = player.x - self.x`, `dy = player.y - self.y`, divide both by the distance `sqrt(dx*dx + dy*dy)`, and multiply by speed for equal speed in all directions.

</details>

> 💡 **NEA link:** comparing two candidate algorithms (sign-comparison vs normalised vector), stating the trade-off, choosing one and justifying it — that paragraph is textbook top-band **justified design**.

### Challenge 21 — Spawning enemies on a timer ★★

**Goal:** Start with no enemies, and spawn a new patrolling enemy at a random height every **two seconds**, up to a maximum of ten.

**Hints**

- pygame can post you a custom event on a schedule: define `SPAWN_ENEMY = pygame.USEREVENT + 1` then call `pygame.time.set_timer(SPAWN_ENEMY, 2000)` (milliseconds).
- Handle it in the event loop like any other event: `if event.type == SPAWN_ENEMY:`.
- Guard with `if len(enemies) < 10:` so the screen doesn't flood.

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = speed

    def update(self):
        self.rect.x = self.rect.x + self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enemy Spawner")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

SPAWN_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY, 2000)   # fire every 2000 ms

enemies = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_ENEMY:
            if len(enemies) < 10:
                y = random.randint(40, HEIGHT - 40)
                speed = random.choice([-4, -3, 3, 4])
                enemies.add(Enemy(20, y, speed))

    enemies.update()

    screen.fill((30, 30, 60))
    enemies.draw(screen)
    count_text = font.render("Enemies: " + str(len(enemies)), True, (255, 255, 255))
    screen.blit(count_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

`set_timer` posts your custom event into the same queue as key presses and mouse clicks, so all timing logic lives in one place — the event loop — rather than counting frames by hand. The `len(enemies) < 10` guard is a designed limit: an unbounded spawner is a slow-motion crash.

</details>

> 💡 **NEA link:** "maximum 10 enemies" is a testable requirement with an obvious boundary test (wait 30 seconds; count). Cap-style limits also evidence you thought about **performance and failure modes**.

### Challenge 22 — Lives and losing them ★★

**Goal:** Give the player **3 lives**. Touching any enemy costs one life and knocks the player back to the centre, with one second of invincibility (the player flashes) so a single touch can't drain all three lives at once. At 0 lives, print `GAME OVER` and stop the enemies moving.

**Hints**

- Use `pygame.sprite.spritecollide(player, enemies, False)` — `False` because enemies survive the collision.
- Invincibility: record `pygame.time.get_ticks()` (milliseconds since start) when hit; ignore collisions until 1000 ms later.
- Flashing: only draw the player on alternate 100 ms slices while invincible — `(pygame.time.get_ticks() // 100) % 2 == 0`.

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = speed

    def update(self):
        self.rect.x = self.rect.x + self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three Lives")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = Player(WIDTH // 2, HEIGHT // 2)
enemies = pygame.sprite.Group()
for i in range(4):
    enemies.add(Enemy(random.randint(40, WIDTH - 40),
                      random.randint(40, HEIGHT - 40),
                      random.choice([-4, -3, 3, 4])))

lives = 3
hit_time = -1000      # long enough ago that we start vulnerable
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    invincible = (now - hit_time) < 1000

    if not game_over:
        player.update()
        enemies.update()
        if not invincible:
            hits = pygame.sprite.spritecollide(player, enemies, False)
            if len(hits) > 0:
                lives = lives - 1
                hit_time = now
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                if lives == 0:
                    game_over = True
                    print("GAME OVER")

    screen.fill((30, 30, 60))
    enemies.draw(screen)
    # flash while invincible: skip drawing on alternate 100 ms slices
    if not invincible or (now // 100) % 2 == 0:
        screen.blit(player.image, player.rect)
    lives_text = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))
    if game_over:
        over_text = font.render("GAME OVER", True, (220, 40, 40))
        over_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(over_text, over_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

The invincibility window fixes a real defect: without it, one overlap fires the collision on 60 consecutive frames and all three lives vanish in a twentieth of a second. Finding a bug like that in playtesting, explaining its cause, and evidencing the fix is prime NEA material.

</details>

> 💡 **NEA link:** write this one up as a full defect report: *symptom* (all lives lost instantly) → *diagnosis* (collision true on consecutive frames) → *fix* (1000 ms invincibility) → *retest*. That narrative is exactly what "testing informing development" means.

### Challenge 23 — Game states: title screen ★★

**Goal:** Add a **title screen** to a game: the program starts on a screen showing the game name and `Press SPACE to start`; pressing space switches to the playing state (use the bouncing ball from Challenge 7 as the "game").

**Hints**

- Hold the current state in a variable, e.g. `state = "title"` / `"playing"`, and branch on it in *both* the update phase and the draw phase.
- The state changes inside the event loop: on `KEYDOWN` of `pygame.K_SPACE` while in `"title"`.
- Only one `while running` loop — the state variable decides what that loop does.

<details><summary>Solution</summary>

```python
import pygame

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Title Screen")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

state = "title"
x, y = WIDTH // 2, HEIGHT // 2
dx, dy = 5, 3
radius = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if state == "title" and event.key == pygame.K_SPACE:
                state = "playing"

    # update — depends on state
    if state == "playing":
        x = x + dx
        y = y + dy
        if x - radius < 0 or x + radius > WIDTH:
            dx = -dx
        if y - radius < 0 or y + radius > HEIGHT:
            dy = -dy

    # draw — depends on state
    screen.fill((30, 30, 60))
    if state == "title":
        title_text = big_font.render("BALL BOUNCER", True, (250, 210, 60))
        prompt_text = font.render("Press SPACE to start", True, (255, 255, 255))
        screen.blit(title_text, title_text.get_rect(center=(WIDTH // 2, 250)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, 350)))
    elif state == "playing":
        pygame.draw.circle(screen, (240, 120, 60), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

This is a **finite state machine**: a variable holding the current state, plus rules for when it transitions. Everything the game does is conditioned on the state, but there is still only one loop and one draw per frame.

</details>

> 💡 **NEA link:** draw the state diagram (states as circles, key presses as arrows) in your Design section. It is quick, it is rigorous, and it makes the following challenge almost write itself.

### Challenge 24 — Game over and restart ★★★

**Goal:** Complete the state machine: **title → playing → game over → (space) → playing again**. Use the lives game from Challenge 22; on game over show the final state and `Press SPACE to play again`. Restarting must fully reset lives, positions and enemies.

**Hints**

- Three states now: `"title"`, `"playing"`, `"game_over"`.
- Write a function `reset_game()` that creates and returns fresh player, enemies, and lives — call it when play starts *and* when it restarts. Never try to "patch up" old state by hand; rebuild it.
- Transition to `"game_over"` where lives hits 0.

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = speed

    def update(self):
        self.rect.x = self.rect.x + self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx

def reset_game():
    """Build a completely fresh game: player, enemies, lives."""
    player = Player(WIDTH // 2, HEIGHT // 2)
    enemies = pygame.sprite.Group()
    for i in range(4):
        enemies.add(Enemy(random.randint(40, WIDTH - 40),
                          random.randint(40, HEIGHT - 40),
                          random.choice([-4, -3, 3, 4])))
    return player, enemies, 3

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Full State Machine")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

state = "title"
player, enemies, lives = reset_game()
hit_time = -1000

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state == "title":
                state = "playing"
            elif state == "game_over":
                player, enemies, lives = reset_game()   # full rebuild
                state = "playing"

    now = pygame.time.get_ticks()
    invincible = (now - hit_time) < 1000

    if state == "playing":
        player.update()
        enemies.update()
        if not invincible:
            hits = pygame.sprite.spritecollide(player, enemies, False)
            if len(hits) > 0:
                lives = lives - 1
                hit_time = now
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                if lives == 0:
                    state = "game_over"

    screen.fill((30, 30, 60))
    if state == "title":
        title_text = big_font.render("DODGE!", True, (250, 210, 60))
        prompt_text = font.render("Press SPACE to start", True, (255, 255, 255))
        screen.blit(title_text, title_text.get_rect(center=(WIDTH // 2, 250)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, 350)))
    elif state == "playing":
        enemies.draw(screen)
        if not invincible or (now // 100) % 2 == 0:
            screen.blit(player.image, player.rect)
        lives_text = font.render("Lives: " + str(lives), True, (255, 255, 255))
        screen.blit(lives_text, (10, 10))
    elif state == "game_over":
        over_text = big_font.render("GAME OVER", True, (220, 40, 40))
        prompt_text = font.render("Press SPACE to play again", True, (255, 255, 255))
        screen.blit(over_text, over_text.get_rect(center=(WIDTH // 2, 250)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, 350)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

The crucial design decision is `reset_game()`: restart bugs ("second game started with 0 lives", "old enemies still on screen") almost always come from resetting *some* variables and forgetting others. Rebuilding everything in one function makes the reset provably complete — and gives you a single place to test.

</details>

> 💡 **NEA link:** restart is a classic source of defects; test it explicitly (play → die → restart → check lives, score, positions all fresh). A test table row per reset item is quick, convincing evidence.

---

## Session 4 (Week 28) — Persistence, Polish, and Your Own Game

The final session adds the feature every arcade game needs — a **persistent high score** — then polishes the game, and hands you mini-project briefs to make something of your own.

### Challenge 25 — Saving the high score ★★

**Goal:** Write two functions: `load_high_score()`, which reads an integer from `highscore.txt` (returning 0 if the file does not exist), and `save_high_score(score)`, which writes it. Test them from a simple console program before touching the game.

**Hints**

- Writing: `with open("highscore.txt", "w") as f: f.write(str(score))` — the `with` block closes the file automatically.
- Reading: wrap in `try:` / `except FileNotFoundError:` — the first ever run has no file, and that must not crash.
- Test the functions *in isolation* first: this is unit-style testing, and it is much faster than replaying the game to trigger each case.

**Example**

```
First run:  high score loaded = 0
Saved 120
Second run: high score loaded = 120
```

<details><summary>Solution</summary>

```python
def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0          # no file yet — first ever run

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# --- test harness ---
print("high score loaded =", load_high_score())
save_high_score(120)
print("after saving 120, loaded =", load_high_score())
save_high_score(45)      # lower score saved deliberately for testing
print("after saving 45, loaded =", load_high_score())
```

Files store *text*, so the score is converted with `str()` on the way out and `int()` on the way back. Note the design question the test harness exposes: should `save_high_score` refuse to save a *lower* score, or is that the caller's job? Either is fine — but decide, and write it down.

</details>

> 💡 **NEA link:** separating file handling into small, independently tested functions is **modular design** — and the "first run, no file" case is a mandatory erroneous-data test for any NEA that touches files.

### Challenge 26 — Loading safely: validation ★★

**Goal:** Harden `load_high_score()` so that a **corrupted** file (empty, or containing `abc`, or `-50`) can never crash the game or produce a nonsense high score. Prove it with a test harness that writes each bad file and calls the function.

**Hints**

- `int()` raises `ValueError` on non-numeric text — catch it alongside `FileNotFoundError`.
- After converting successfully, validate the *range*: a negative high score fails a sanity check; return 0 instead.
- The test harness should create each corrupt file deliberately — never rely on "it probably won't happen".

**Example**

```
missing file      -> 0
empty file        -> 0
'abc' in file     -> 0
'-50' in file     -> 0
'120' in file     -> 120
```

<details><summary>Solution</summary>

```python
import os

def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            value = int(f.read())
    except (FileNotFoundError, ValueError):
        return 0              # missing file, empty file or non-numeric content
    if value < 0:
        return 0              # range check: a negative high score is invalid
    return value

def write_test_file(content):
    with open("highscore.txt", "w") as f:
        f.write(content)

# --- test harness: erroneous, boundary and normal data ---
if os.path.exists("highscore.txt"):
    os.remove("highscore.txt")
print("missing file      ->", load_high_score())

write_test_file("")
print("empty file        ->", load_high_score())

write_test_file("abc")
print("'abc' in file     ->", load_high_score())

write_test_file("-50")
print("'-50' in file     ->", load_high_score())

write_test_file("120")
print("'120' in file     ->", load_high_score())
```

Two layers of defence: **exception handling** for things that stop conversion working at all, then a **range check** on values that convert but make no sense. `int("")` raises `ValueError` too, so the empty file is caught by the same `except`.

</details>

> 💡 **NEA link:** this challenge *is* an NEA test table — erroneous (`abc`), boundary (`-50`, empty) and normal (`120`) data with expected and actual results. Reuse the harness pattern for every file or input routine in your project.

### Challenge 27 — A top-five high-score table ★★★

**Goal:** Upgrade to a score *table*: store the top five `name,score` pairs in `scores.csv`, highest first. Write functions to load the table, add a new entry (keeping only the top five), save it, and display it neatly.

**Hints**

- Store one entry per line as `name,score`; split with `line.split(",")`.
- Keep the table as a list of `[name, score]` lists. Sort descending with `table.sort(key=get_score, reverse=True)` where `get_score` returns the numeric score, then slice `[:5]`.
- Skip malformed lines when loading (wrong number of fields, non-numeric score) — files edited by humans get corrupted.

**Example**

```
== HIGH SCORES ==
1. Maya ....... 310
2. Tom ........ 250
3. Priya ...... 180
4. Sam ........ 120
5. Alex ....... 90
```

<details><summary>Solution</summary>

```python
def get_score(entry):
    return entry[1]

def load_table():
    table = []
    try:
        with open("scores.csv", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        table.append([parts[0], int(parts[1])])
                    except ValueError:
                        pass          # non-numeric score — skip the bad line
    except FileNotFoundError:
        pass                          # no table yet — return empty
    table.sort(key=get_score, reverse=True)
    return table[:5]

def save_table(table):
    with open("scores.csv", "w") as f:
        for entry in table:
            f.write(entry[0] + "," + str(entry[1]) + "\n")

def add_score(table, name, score):
    table.append([name, score])
    table.sort(key=get_score, reverse=True)
    return table[:5]                  # keep only the best five

def display_table(table):
    print("== HIGH SCORES ==")
    for i in range(len(table)):
        name, score = table[i]
        print(str(i + 1) + ". " + name.ljust(10, ".") + " " + str(score))

# --- demo / test ---
table = load_table()
for name, score in [("Maya", 310), ("Tom", 250), ("Priya", 180),
                    ("Sam", 120), ("Alex", 90), ("Jo", 60)]:
    table = add_score(table, name, score)
save_table(table)
display_table(table)
print("Jo (60) correctly squeezed out:", len(table) == 5)
```

Four small functions, each doing one job, sharing one data structure (a list of `[name, score]` lists). To show the table *inside* the game, loop over `load_table()` rendering one font line per entry at increasing y positions — the drawing skill is Challenge 15.

</details>

> 💡 **NEA link:** records persisted to file, parsed, validated, sorted and truncated — in one small feature you have evidenced **file handling, a data structure decision, a sorting requirement and defensive parsing**. Flag each explicitly in your annotations; moderators cannot credit what you do not point out.

### Challenge 28 — Polish: pause and rising difficulty ★★

**Goal:** Add two professional touches to the enemies game: pressing **P** pauses/unpauses (frozen action, `PAUSED` overlay), and the game gets harder the longer you survive — every 10 seconds, all enemies speed up by 10%.

**Hints**

- Pause is just another state — but a Boolean `paused` flag alongside the main state works well: when `True`, skip the update phase but still draw.
- Toggle with `paused = not paused` on the P `KEYDOWN`.
- For the ramp, keep `next_ramp` as a time in milliseconds; when `pygame.time.get_ticks()` passes it, multiply every enemy's speed and add 10 000 to `next_ramp`. (Careful: pausing does not stop `get_ticks()` — acceptable here, but worth noting as a known limitation.)

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = speed

    def update(self):
        self.rect.x = self.rect.x + self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx

    def speed_up(self, factor):
        self.dx = self.dx * factor

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pause + Difficulty Ramp")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

enemies = pygame.sprite.Group()
for i in range(5):
    enemies.add(Enemy(random.randint(40, WIDTH - 40),
                      random.randint(40, HEIGHT - 40),
                      random.choice([-4, -3, 3, 4])))

paused = False
next_ramp = 10000        # first speed-up after 10 seconds
level = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            paused = not paused          # toggle

    now = pygame.time.get_ticks()

    if not paused:
        enemies.update()
        if now >= next_ramp:
            for enemy in enemies:
                enemy.speed_up(1.1)      # 10% faster
            level = level + 1
            next_ramp = next_ramp + 10000

    screen.fill((30, 30, 60))
    enemies.draw(screen)
    level_text = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(level_text, (10, 10))
    if paused:
        pause_text = big_font.render("PAUSED", True, (250, 210, 60))
        screen.blit(pause_text, pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Note that pausing skips *updating* but never *drawing* — the frame must keep rendering or the window stops responding. The comment about `get_ticks()` continuing during pause is an honest **known limitation**: stating limitations you understand is worth more than pretending there are none.

</details>

> 💡 **NEA link:** difficulty tuning is a genuine **stakeholder feedback loop** — playtesters say "too easy/too hard", you adjust the ramp constants, you retest. Record before/after values and the tester's verdicts as Evaluation-grade evidence.

### Challenge 29 — Coin Chaser: the final build ★★★

**Goal:** Assemble everything from all four sessions into one finished game. Requirements: title, playing and game-over states; arrow-key player; coins worth 10 (all collected → respawn a fresh set); one patrolling enemy per 50 points, up to 6; 3 lives with invincibility flashes; live score, lives and high score on screen; high score loaded at start and saved (only if beaten) at game over; full reset on replay.

**Hints**

- Do not write this from scratch — **integrate** Challenges 16, 22, 24, 25/26. Most of it is copy-in and reconcile.
- Keep `load_high_score()` / `save_high_score()` from Challenge 26 exactly as tested.
- Work through the requirement list one at a time, testing after each — never bolt on three features untested.

<details><summary>Solution</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_UP]:
            self.rect.y = self.rect.y - self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (250, 210, 60), (10, 10), 10)
        self.rect = self.image.get_rect(
            center=(random.randint(10, WIDTH - 10),
                    random.randint(10, HEIGHT - 10)))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(
            center=(20, random.randint(40, HEIGHT - 40)))
        self.dx = random.choice([-4, -3, 3, 4])

    def update(self):
        self.rect.x = self.rect.x + self.dx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx = -self.dx

def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            value = int(f.read())
    except (FileNotFoundError, ValueError):
        return 0
    if value < 0:
        return 0
    return value

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def spawn_coins(coins, amount):
    for i in range(amount):
        coins.add(Coin())

def reset_game():
    player = Player(WIDTH // 2, HEIGHT // 2)
    coins = pygame.sprite.Group()
    spawn_coins(coins, 10)
    enemies = pygame.sprite.Group()
    return player, coins, enemies, 0, 3     # score, lives

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Chaser")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

state = "title"
high_score = load_high_score()
player, coins, enemies, score, lives = reset_game()
hit_time = -1000

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state in ("title", "game_over"):
                player, coins, enemies, score, lives = reset_game()
                state = "playing"

    now = pygame.time.get_ticks()
    invincible = (now - hit_time) < 1000

    if state == "playing":
        player.update()
        enemies.update()

        grabbed = pygame.sprite.spritecollide(player, coins, True)
        score = score + len(grabbed) * 10
        if len(coins) == 0:
            spawn_coins(coins, 10)          # fresh field — the game is endless

        # one enemy per 50 points, capped at 6
        target_enemies = min(score // 50, 6)
        while len(enemies) < target_enemies:
            enemies.add(Enemy())

        if not invincible:
            hits = pygame.sprite.spritecollide(player, enemies, False)
            if len(hits) > 0:
                lives = lives - 1
                hit_time = now
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                if lives == 0:
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)
                    state = "game_over"

    screen.fill((30, 30, 60))
    if state == "title":
        title_text = big_font.render("COIN CHASER", True, (250, 210, 60))
        prompt_text = font.render("Press SPACE to start", True, (255, 255, 255))
        hs_text = font.render("High score: " + str(high_score), True, (255, 255, 255))
        screen.blit(title_text, title_text.get_rect(center=(WIDTH // 2, 220)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, 320)))
        screen.blit(hs_text, hs_text.get_rect(center=(WIDTH // 2, 380)))
    elif state == "playing":
        coins.draw(screen)
        enemies.draw(screen)
        if not invincible or (now // 100) % 2 == 0:
            screen.blit(player.image, player.rect)
        hud = "Score: " + str(score) + "   Lives: " + str(lives) \
              + "   Best: " + str(high_score)
        screen.blit(font.render(hud, True, (255, 255, 255)), (10, 10))
    elif state == "game_over":
        over_text = big_font.render("GAME OVER", True, (220, 40, 40))
        score_text = font.render("Score: " + str(score) +
                                 "   High score: " + str(high_score),
                                 True, (255, 255, 255))
        prompt_text = font.render("Press SPACE to play again", True, (255, 255, 255))
        screen.blit(over_text, over_text.get_rect(center=(WIDTH // 2, 220)))
        screen.blit(score_text, score_text.get_rect(center=(WIDTH // 2, 320)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, 380)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Around 140 lines for a complete, robust, persistent game — every piece of which you built and tested separately first. The enemy-count rule (`min(score // 50, 6)`) is one line, but it is a *designed difficulty curve*: instantly tunable, easily testable ("at score 100 there are exactly 2 enemies").

</details>

> 💡 **NEA link:** this build order — components tested in isolation, then integrated one requirement at a time — is precisely the **iterative development** narrative worth the most Development marks. Keep dated screenshots of *each* integration step, not just the final game.

### Challenge 30 — Extension mini-projects: your own game ★★★

**Goal:** Choose **one** brief below and build it using only techniques from this workbook. Before writing any code, write the NEA-style scaffolding: 4–6 measurable success criteria, a decomposition list, and a test plan of at least 8 rows (normal / boundary / erroneous). Then develop it in evidenced iterations.

**Brief A — Dodger.** Blocks fall from the top of the screen at random x positions and speeds; the player moves left/right along the bottom to avoid them. Score = survival time in seconds. Falling speed ramps up over time. High score persists between runs.

**Brief B — Snake.** A snake moves on a grid, growing by one segment per item eaten; the game ends if it hits a wall or itself. *Data structure hint:* the snake is a **list of grid positions** — insert the new head at the front, and remove the tail unless the snake just ate.

**Brief C — Breakout.** A paddle bounces a ball up into a wall of bricks; each brick vanishes when hit (ball's vertical direction reverses). Lose a life when the ball falls off the bottom; clear all bricks to win. *Stretch:* bounce angle depends on where the ball strikes the paddle.

**Brief D — Space Shooter.** The player's ship moves along the bottom firing bullets (space bar, rate-limited); enemies spawn at the top and descend. Bullets destroy enemies (+10); an enemy reaching the bottom or touching the ship costs a life. *Data structure hint:* one sprite group for bullets, one for enemies — `pygame.sprite.groupcollide(bullets, enemies, True, True)` handles all bullet-enemy collisions in one call.

**Hints**

- Every mechanic in every brief maps onto a challenge you have completed — falling blocks are Challenge 21 spawning + Challenge 6 movement; bullets are player-created sprites in a group (Challenge 10); grid movement is Challenge 6 with a step size of one cell.
- Start with the smallest playable version (player moves + one hazard + game over), then iterate.

<details><summary>Solution — model answer for Brief A (Dodger)</summary>

```python
import pygame
import random

WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill((80, 200, 120))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

class Block(pygame.sprite.Sprite):
    def __init__(self, speed_bonus):
        super().__init__()
        size = random.randint(20, 50)
        self.image = pygame.Surface((size, size))
        self.image.fill((220, 40, 40))
        self.rect = self.image.get_rect(
            midbottom=(random.randint(25, WIDTH - 25), 0))
        self.dy = random.randint(3, 6) + speed_bonus

    def update(self):
        self.rect.y = self.rect.y + self.dy
        if self.rect.top > HEIGHT:
            self.kill()                 # off screen — remove from all groups

def load_high_score():
    try:
        with open("dodger-highscore.txt", "r") as f:
            value = int(f.read())
    except (FileNotFoundError, ValueError):
        return 0
    if value < 0:
        return 0
    return value

def save_high_score(score):
    with open("dodger-highscore.txt", "w") as f:
        f.write(str(score))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

SPAWN_BLOCK = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BLOCK, 600)   # a new block every 0.6 s

state = "title"
high_score = load_high_score()
player = Player()
blocks = pygame.sprite.Group()
start_time = 0
survived = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state in ("title", "game_over"):
                player = Player()
                blocks.empty()
                start_time = pygame.time.get_ticks()
                state = "playing"
        elif event.type == SPAWN_BLOCK and state == "playing":
            speed_bonus = (pygame.time.get_ticks() - start_time) // 10000
            blocks.add(Block(speed_bonus))   # blocks get faster over time

    if state == "playing":
        player.update()
        blocks.update()
        survived = (pygame.time.get_ticks() - start_time) // 1000
        if pygame.sprite.spritecollide(player, blocks, False):
            if survived > high_score:
                high_score = survived
                save_high_score(high_score)
            state = "game_over"

    screen.fill((30, 30, 60))
    if state == "title":
        title_text = big_font.render("DODGER", True, (250, 210, 60))
        prompt_text = font.render("Press SPACE to start", True, (255, 255, 255))
        hs_text = font.render("Best: " + str(high_score) + " s", True, (255, 255, 255))
        screen.blit(title_text, title_text.get_rect(center=(WIDTH // 2, 220)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, 320)))
        screen.blit(hs_text, hs_text.get_rect(center=(WIDTH // 2, 380)))
    elif state == "playing":
        blocks.draw(screen)
        screen.blit(player.image, player.rect)
        hud = "Time: " + str(survived) + " s   Best: " + str(high_score) + " s"
        screen.blit(font.render(hud, True, (255, 255, 255)), (10, 10))
    elif state == "game_over":
        over_text = big_font.render("GAME OVER", True, (220, 40, 40))
        result_text = font.render("You survived " + str(survived) +
                                  " s   Best: " + str(high_score) + " s",
                                  True, (255, 255, 255))
        prompt_text = font.render("Press SPACE to play again", True, (255, 255, 255))
        screen.blit(over_text, over_text.get_rect(center=(WIDTH // 2, 220)))
        screen.blit(result_text, result_text.get_rect(center=(WIDTH // 2, 320)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH // 2, 380)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Sample success criteria for Brief A (yours should look like this — each one testable): (1) the player cannot leave the screen; (2) a new block spawns every 0.6 s ± 0.1 s while playing; (3) blocks that leave the screen are removed (block count never grows unbounded); (4) block base speed rises by 1 for every 10 s survived; (5) any overlap between player and block ends the game within one frame; (6) the best survival time persists after the program is closed and reopened, and a corrupt high-score file loads as 0. Note `self.kill()` in `Block.update()` — criterion 3 depends on it, and forgetting it is *the* classic spawner memory leak.

</details>

> 💡 **NEA link:** the brief-first workflow here — measurable criteria, decomposition and a test plan *before* code — is a dress rehearsal for the real project. If you keep your criteria list, iteration screenshots and test tables for this mini-project, you will have practised producing every artefact the NEA Analysis, Design, Development and Evaluation sections demand.

---

## Where next

You now have every practical skill a game-style NEA needs: the event loop, OOP sprites, collision algorithms, state machines, and validated file persistence.

- **NEA Guide** (in this folder) — how the four assessed stages are marked and how to turn what you built here into top-band evidence.
- **Programming Workbooks 1 and 2** — the core techniques and the searching/sorting algorithms your project's "computational complexity" can draw on.
- Keep your mini-project. A polished Challenge 30 game, with its criteria, iterations and tests, is a working model of the whole NEA process in miniature.
