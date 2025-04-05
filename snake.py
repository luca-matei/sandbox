import pygame
import random

pygame.init()
screen_x = 1260  # Latimea ecranului in px
screen_y = 720  # Inaltimea ecranului in px
screen_size = (screen_x, screen_y)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

l_patrat = 30  # Latimea unui patrat in px
patrate_x = int(screen_x / l_patrat)
patrate_y = int(screen_y / l_patrat)
snake_sq = [2, 3]
apple_sq = [4, 5]
direction = "right"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    if direction == "up":
        snake_sq[1] -= 1
    elif direction == "right":
        snake_sq[0] += 1
    elif direction == "down":
        snake_sq[1] += 1
    elif direction == "left":
        snake_sq[0] -= 1

    # Check for collision with walls
    # Marginea de sus
    if snake_sq[1] == -1:
        snake_sq[1] = patrate_y - 1
    # Marginea din stanga
    elif snake_sq[0] == -1:
        snake_sq[0] = patrate_x - 1
    # Marginea de jos
    elif snake_sq[1] == patrate_y:
        snake_sq[1] = 0
    # Marginea din dreapta
    elif snake_sq[0] == patrate_x:
        snake_sq[0] = 0

    # Check for collision with apple
    if snake_sq == apple_sq:
        apple_sq[0] = random.randint(0, patrate_x - 1)
        apple_sq[1] = random.randint(0, patrate_y - 1)

    screen.fill("yellow")

    for i in range(0, patrate_x):
        for j in range(0, patrate_y):
            pygame.draw.rect(screen, "#eeee00", (i * l_patrat, j * l_patrat, l_patrat, l_patrat), 1)

    # Apple
    pygame.draw.rect(screen, "red", (apple_sq[0] * l_patrat, apple_sq[1] * l_patrat, l_patrat, l_patrat))

    # Snake
    pygame.draw.rect(screen, "green", (snake_sq[0] * l_patrat, snake_sq[1] * l_patrat, l_patrat, l_patrat))

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
