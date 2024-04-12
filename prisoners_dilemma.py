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
PRIMARY = (119, 113, 238)
SECONDARY = (69, 60, 103)
BUTTON_COLOR = (70, 194, 203)
BUTTON_HOVER_COLOR = (242, 247, 161)
BUTTON_BORDER_COLOR = (69, 60, 103)
TEXT_COLOR = SECONDARY

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
        screen.fill(PRIMARY)
        draw_text("Prisoners Dilemma", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 90)
        draw_text("Simulator", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 150)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Buttons
        buttons = [
            {"text": "Start", "rect": pygame.Rect(screen_width // 2 - 150, 200, 300, 60)},
            {"text": "Instructions", "rect": pygame.Rect(screen_width // 2 - 150, 300, 300, 60)},
            {"text": "Theory", "rect": pygame.Rect(screen_width // 2 - 150, 400, 300, 60)},
            {"text": "Quit", "rect": pygame.Rect(screen_width // 2 - 150, 500, 300, 60)}
        ]

        # Highlight the button when mouse is over it
        for button in buttons:
            if button["rect"].collidepoint((mouse_x, mouse_y)):
                pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 3)  # Add border
            else:
                pygame.draw.rect(screen, BUTTON_COLOR, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 3)  # Add border
            draw_text(button["text"], font, TEXT_COLOR, button["rect"].centerx, button["rect"].centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint((mouse_x, mouse_y)):
                        if button["text"] == "Start":
                            # Start the game
                            # Replace this with your actual game code
                            print("Starting game...")
                        elif button["text"] == "Instructions":
                            # Show instructions
                            show_instructions()
                        elif button["text"] == "Theory":
                            # Show theory
                            # Replace this with your theory display code
                            print("Showing theory...")
                        elif button["text"] == "Quit":
                            pygame.quit()
                            sys.exit()

        pygame.display.update()

# Function to display the instructions
def show_instructions():
    running = True
    while running:
        screen.fill(PRIMARY)
        draw_text("Instructions", font, TEXT_COLOR, screen_width // 2, 50)
        
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
            draw_text(text, instruction_font, TEXT_COLOR, screen_width // 2, y_offset)
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
