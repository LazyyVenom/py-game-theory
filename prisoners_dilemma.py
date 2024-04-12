import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prisoner's Dilemma")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)

# Fonts
font = pygame.font.Font(None, 50)
instruction_font = pygame.font.Font(None, 30)

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to display the menu
def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Menu", font, BLACK, screen_width // 2, 100)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Buttons
        button_width = 250
        button_height = 50
        button_start = pygame.Rect(screen_width // 2 - button_width // 2, 200, button_width, button_height)
        button_instructions = pygame.Rect(screen_width // 2 - button_width // 2, 300, button_width, button_height)
        button_theory = pygame.Rect(screen_width // 2 - button_width // 2, 400, button_width, button_height)
        button_quit = pygame.Rect(screen_width // 2 - button_width // 2, 500, button_width, button_height)

        # Highlight the button when mouse is over it
        if button_start.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_start)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_start)

        if button_instructions.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_instructions)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_instructions)

        if button_theory.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_theory)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_theory)

        if button_quit.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_quit)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_quit)

        draw_text("Start", font, WHITE, button_start.centerx, button_start.centery)
        draw_text("Instructions", font, WHITE, button_instructions.centerx, button_instructions.centery)
        draw_text("Theory", font, WHITE, button_theory.centerx, button_theory.centery)
        draw_text("Quit", font, WHITE, button_quit.centerx, button_quit.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint((mouse_x, mouse_y)):
                    # Start the game
                    # Replace this with your actual game code
                    print("Starting game...")
                if button_instructions.collidepoint((mouse_x, mouse_y)):
                    # Show instructions
                    show_instructions()
                if button_theory.collidepoint((mouse_x, mouse_y)):
                    # Show theory
                    # Replace this with your theory display code
                    print("Showing theory...")
                if button_quit.collidepoint((mouse_x, mouse_y)):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Function to display the instructions
def show_instructions():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Instructions", font, BLACK, screen_width // 2, 50)
        
        # Display the instructions content
        instruction_text = [
            "Welcome to the instructions page!",
            "",
            "Here you can add your instructions content.",
            "Use arrow keys to move, space to jump, etc.",
            "",
            "Press 'Esc' to return to the main menu."
        ]
        y_offset = 150
        for text in instruction_text:
            draw_text(text, instruction_font, BLACK, screen_width // 2, y_offset)
            y_offset += 30

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

# Run the main menu
main_menu()
