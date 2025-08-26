import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Movement Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sprite dimensions
SPRITE_WIDTH, SPRITE_HEIGHT = 50, 50

# Create two rectangles (sprites)
player_rect = pygame.Rect(100, 100, SPRITE_WIDTH, SPRITE_HEIGHT)  # Controlled sprite
static_rect = pygame.Rect(400, 300, SPRITE_WIDTH, SPRITE_HEIGHT)  # Static sprite

# Movement speed
speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Controls frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Fill screen and draw sprites
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, BLUE, static_rect)

    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()