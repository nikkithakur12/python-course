import pygame
import random

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Dodger")
clock = pygame.time.Clock()

# --- Entities ---
player = pygame.Rect(180, 440, 40, 40)
enemy = pygame.Rect(random.randint(0, 360), -50, 40, 40)
enemy_speed = 5
score = 0

# --- Main Loop ---
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 7
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 7

    # 3. Enemy Logic
    enemy.y += enemy_speed
    if enemy.top > HEIGHT:  # Reset enemy when it falls off screen
        enemy.y = -50
        enemy.x = random.randint(0, 360)
        score += 1
        enemy_speed += 0.2  # Make it get harder!

    # 4. Collision Detection
    if player.colliderect(enemy):
        print(f"Game Over! Final Score: {score}")
        running = False

    # 5. Drawing
    screen.fill((255, 255, 255))      # White Background
    pygame.draw.rect(screen, (0, 100, 255), player)  # Blue Player
    pygame.draw.rect(screen, (255, 50, 50), enemy)   # Red Enemy
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()