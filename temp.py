import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Page")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 32)

# Checkboxes
checkbox1 = pygame.Rect(50, 100, 20, 20)
checkbox2 = pygame.Rect(50, 150, 20, 20)
checkbox1_checked = False
checkbox2_checked = False

# Input field
input_rect = pygame.Rect(150, 100, 140, 40)
input_text = ''
input_selected = False

# Main loop
while True:
    screen.fill(WHITE)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Checkbox 1
                if checkbox1.collidepoint(event.pos):
                    checkbox1_checked = not checkbox1_checked
                # Checkbox 2
                elif checkbox2.collidepoint(event.pos):
                    checkbox2_checked = not checkbox2_checked
                # Input field
                elif input_rect.collidepoint(event.pos):
                    input_selected = True
                else:
                    input_selected = False
        if event.type == pygame.KEYDOWN:
            # Input field
            if input_selected:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Draw checkboxes
    pygame.draw.rect(screen, BLACK, checkbox1, 2)
    pygame.draw.rect(screen, BLACK, checkbox2, 2)
    if checkbox1_checked:
        pygame.draw.line(screen, BLACK, (checkbox1.left + 3, checkbox1.centery), (checkbox1.right - 3, checkbox1.centery), 2)
    if checkbox2_checked:
        pygame.draw.line(screen, BLACK, (checkbox2.left + 3, checkbox2.centery), (checkbox2.right - 3, checkbox2.centery), 2)

    # Draw input field
    if input_selected:
        pygame.draw.rect(screen, GREEN, input_rect, 2)
    else:
        pygame.draw.rect(screen, BLACK, input_rect, 2)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    pygame.display.flip()