import pygame
import random

pygame.init()
window_x = 1260  # Window width in px
window_y = 720  # Window height in px
screen = pygame.display.set_mode((window_x, window_y))
clock = pygame.time.Clock()
running = True

x = 2
y = 3

sq_size = 30  # Square size in px
sqrs_x = int(window_x / sq_size)  # Number of squares in x snake_dir
sqrs_y = int(window_y / sq_size)  # Number of squares in y snake_dir


snake_pos = [ [x, y] , [1, 3]] # Snake position
apple_pos = [4, 5]  # Apple position
snake_dir = "right"  # Snake direction

while running:
    for event in pygame.event.get():
        # Check for quit window event
        if event.type == pygame.QUIT:
            running = False

        # Check for key press event
        elif event.type == pygame.KEYDOWN:
            # ESCAPE key to quit
            if event.key == pygame.K_ESCAPE:
                running = False

            # Arrow keys to change direction
            # Note: We check for the opposite direction to prevent the snake from going back on itself
            elif event.key == pygame.K_UP and snake_dir != "down":
                snake_dir = "up"
            elif event.key == pygame.K_LEFT and snake_dir != "right":
                snake_dir = "left"
            elif event.key == pygame.K_RIGHT and snake_dir != "left":
                snake_dir = "right"
            elif event.key == pygame.K_DOWN and snake_dir != "up":
                snake_dir = "down"


    # Move snake
    if snake_dir == "up":
        y -= 1
    elif snake_dir == "right":
        x += 1
    elif snake_dir == "down":
        y += 1
    elif snake_dir == "left":
        x -= 1

    snake_pos =[ [x, y] ] + snake_pos[:-1]

    # Check for collision with walls
    # Upper margin
    if y == -1:
        y = sqrs_y - 1
    # Left margin
    elif x == -1:
        x = sqrs_x - 1
    # Lower margin
    elif y == sqrs_y:
        y = 0
    # Right margin
    elif x == sqrs_x:
        x = 0

    # Check for collision with apple
    if snake_pos == apple_pos:
        # Generate new apple position
        apple_pos[0] = random.randint(0, sqrs_x - 1)
        apple_pos[1] = random.randint(0, sqrs_y - 1)
    #Adauga un patrat

    # Render background
    screen.fill("yellow")

    # Render grid
    for i in range(0, sqrs_x):
        for j in range(0, sqrs_y):
            pygame.draw.rect(
                screen, "#eeee00", (i * sq_size, j * sq_size, sq_size, sq_size), 1
            )

    # Render Apple
    pygame.draw.rect(
        screen,
        "red",
        (apple_pos[0] * sq_size, apple_pos[1] * sq_size, sq_size, sq_size),
    )

    # Render Snake
    for square_pos in snake_pos:
        pygame.draw.rect(
            screen,
            "green",
            (square_pos[0] * sq_size, square_pos[1] * sq_size, sq_size, sq_size),
        )

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
