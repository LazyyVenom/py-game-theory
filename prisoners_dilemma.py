import pygame
import sys
from strategy import strategies

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
        draw_text("Prisoners Dilemma", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 80)
        draw_text("Simulator", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 150)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        buttons = [
            {"text": "Tournament", "rect": pygame.Rect(screen_width // 2 - 150, 200, 300, 60)},
            {"text": "Simulation", "rect": pygame.Rect(screen_width // 2 - 150, 300, 300, 60)},
            {"text": "Theory", "rect": pygame.Rect(screen_width // 2 - 150, 400, 300, 60)},
            {"text": "Quit", "rect": pygame.Rect(screen_width // 2 - 150, 500, 300, 60)}
        ]

        for button in buttons:
            if button["rect"].collidepoint((mouse_x, mouse_y)):
                pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 3) 
            else:
                pygame.draw.rect(screen, BUTTON_COLOR, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 3)  
            draw_text(button["text"], font, TEXT_COLOR, button["rect"].centerx, button["rect"].centery)

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
                            print("Showing theory...")
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
        {"NAME":strategy.name,
         "ID":strategy.st_id,
         "DESCRIPTION":strategy.desc 
        } for strategy in [strategies[0]] 
    ]

    
    while running:
        screen.fill(PRIMARY)
        draw_text("Theory", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 50)

        y_offset = 100
        for i, strategy in enumerate(instruction_text[scroll_pos:]):
            # for key, value in strategy.items():
            draw_text("NAME", instruction_font, INSTRUCTION_HEADING_COLOR, 50, y_offset)
            draw_text("ID", instruction_font, INSTRUCTION_HEADING_COLOR, 30, y_offset+30)
            draw_text("DESCRIPTION", instruction_font, INSTRUCTION_HEADING_COLOR, 90, y_offset+60)
            
            # draw_text(value, instruction_font, INSTRUCTION_COLOR, 200, y_offset)
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
