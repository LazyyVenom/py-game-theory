import pygame
import sys
from strategy import strategies
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1200
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prisoner's Dilemma")

# Colors
PRIMARY = (119, 113, 238)
SECONDARY = (69, 60, 103)
BUTTON_COLOR = (70, 194, 203)
BUTTON_HOVER_COLOR = (242, 247, 161)
BUTTON_BORDER_COLOR = (69, 60, 103)
TEXT_COLOR = SECONDARY
INSTRUCTION_COLOR = SECONDARY
INSTRUCTION_HEADING_COLOR = (242, 247, 161)

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
        draw_text("Prisoners Dilemma".upper(), pygame.font.Font(None, 110), TEXT_COLOR, screen_width // 2, 100)
        draw_text("Simulator".upper(), pygame.font.Font(None, 110), TEXT_COLOR, screen_width // 2, 170)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        buttons = [
            {"text": "Tournament", "rect": pygame.Rect(screen_width // 2 - 200, 260, 400, 80)},
            {"text": "Simulation", "rect": pygame.Rect(screen_width // 2 - 200, 360, 400, 80)},
            {"text": "Theory", "rect": pygame.Rect(screen_width // 2 - 200, 460, 400, 80)},
            {"text": "Quit", "rect": pygame.Rect(screen_width // 2 - 200, 560, 400, 80)}
        ]

        for button in buttons:
            if button["rect"].collidepoint((mouse_x, mouse_y)):
                pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 6) 
            else:
                pygame.draw.rect(screen, BUTTON_COLOR, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 6)  
            draw_text(button["text"], pygame.font.Font(None, 60), TEXT_COLOR, button["rect"].centerx, button["rect"].centery)

        draw_text("Created Anubhav Choubey", pygame.font.Font(None, 40), BUTTON_HOVER_COLOR, 970, 720)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint((mouse_x, mouse_y)):
                        if button["text"] == "Tournament":
                            # Start the game
                            # Replace this with your actual game code
                            print("Starting game...")
                        elif button["text"] == "Simulation":
                            # Show Simulation
                            print("Starting Simulation")
                        elif button["text"] == "Theory":
                            show_theory()
                            # Show theory
                            # Replace this with your theory display code
                        elif button["text"] == "Quit":
                            pygame.quit()
                            sys.exit()

        pygame.display.update()

# Function to display the Simulation
def show_theory():
    running = True
    scroll_pos = 0 
    scroll_speed = 1  
    instruction_text = [
        {"NAME": strategy.name,
         "ID": strategy.st_id,
         "DESCRIPTION": strategy.desc,
         "IMAGE_PATH": os.path.join("images", f"{strategy.st_id}.png")
        } for strategy in [strategies[0]] 
    ]

    while running:
        screen.fill(PRIMARY)
        draw_text("Theory", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 50)

        y_offset = 100
        for i, strategy in enumerate(instruction_text[scroll_pos:]):
            draw_text(strategy["NAME"], instruction_font, INSTRUCTION_HEADING_COLOR, 50, y_offset)
            draw_text(strategy["ID"], instruction_font, INSTRUCTION_HEADING_COLOR, 30, y_offset+30)
            draw_text(strategy["DESCRIPTION"], instruction_font, INSTRUCTION_HEADING_COLOR, 90, y_offset+60)
            
            # Load and display image if it exists
            image_path = strategy["IMAGE_PATH"]
            if os.path.exists(image_path):
                image = pygame.image.load(image_path)
                screen.blit(image, (400, y_offset))  # Adjust the position as needed
            
            y_offset += 30
            if y_offset > screen_height - 30:
                break

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    if scroll_pos > 0:
                        scroll_pos -= 1  
                elif event.key == pygame.K_DOWN:
                    if scroll_pos < len(instruction_text) - (screen_height - 180) // 30:
                        scroll_pos += 1 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_pos -= scroll_speed
                elif event.button == 5: 
                    scroll_pos += scroll_speed

if __name__ == '__main__':
    main_menu()
