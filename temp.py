import pygame
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 30)

# Sample data
data = {
    "name": "John Doe",
    "id": "123456",
    "image_path": "images/TFT.png",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}

# Load image
image_path = data["image_path"]
if os.path.exists(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (200, 200))
else:
    raise FileNotFoundError(f"Image file '{image_path}' not found")

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle Display")

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLACK, (50, 50, 1100, 200))

    # Display image
    screen.blit(image, (50, 50))

    # Display text
    text_y = 60
    for key, value in data.items():
        if key != "image_path":
            text_surface = font.render(f"{key.capitalize()}: {value}", True, WHITE)
            screen.blit(text_surface, (270, text_y))
            text_y += 30

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

# Quit Pygame
pygame.quit()
