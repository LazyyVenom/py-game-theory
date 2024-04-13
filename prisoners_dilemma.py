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
            {"text": "Tournament", "rect": pygame.Rect(screen_width // 2 - 150, 200, 300, 60)},
            {"text": "Simulation", "rect": pygame.Rect(screen_width // 2 - 150, 300, 300, 60)},
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
    scroll_pos = 0  # Initial scroll position
    scroll_speed = 1  # Adjust scroll speed as needed
    instruction_text = [
        "Welcome to the Theory page!",
        "",
        "Here you can add your Simulation content.",
        "Use arrow keys to move, space to jump, etc.",
        "",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vitae augue vehicula venenatis. Duis elementum id metus vel eleifend. Nam eget magna convallis, gravida magna id, lobortis turpis. Fusce vehicula turpis non neque venenatis, ac feugiat ex blandit. Nullam consequat, libero et tincidunt ullamcorper, libero arcu tincidunt sapien, ut mattis erat odio nec nisl. Ut ac congue risus, in facilisis orci. Nulla in urna et eros ullamcorper vestibulum eget vel mi. Phasellus et quam in nunc interdum eleifend. Aenean molestie, sapien in volutpat viverra, dui enim congue justo, vitae varius turpis ligula id felis. Sed vehicula aliquet quam, ac dapibus lorem pellentesque nec. Sed nec dolor vitae urna tempor tempus non vel magna. Nullam pulvinar sit amet enim eu viverra. Morbi sed dapibus elit.",
        "",
        "Welcome to the Theory page!",
        "",
        "Here you can add your Simulation content.",
        "Use arrow keys to move, space to jump, etc.",
        "",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vitae augue vehicula venenatis. Duis elementum id metus vel eleifend. Nam eget magna convallis, gravida magna id, lobortis turpis. Fusce vehicula turpis non neque venenatis, ac feugiat ex blandit. Nullam consequat, libero et tincidunt ullamcorper, libero arcu tincidunt sapien, ut mattis erat odio nec nisl. Ut ac congue risus, in facilisis orci. Nulla in urna et eros ullamcorper vestibulum eget vel mi. Phasellus et quam in nunc interdum eleifend. Aenean molestie, sapien in volutpat viverra, dui enim congue justo, vitae varius turpis ligula id felis. Sed vehicula aliquet quam, ac dapibus lorem pellentesque nec. Sed nec dolor vitae urna tempor tempus non vel magna. Nullam pulvinar sit amet enim eu viverra. Morbi sed dapibus elit.",
        "",
        "Welcome to the Theory page!",
        "",
        "Here you can add your Simulation content.",
        "Use arrow keys to move, space to jump, etc.",
        "",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vitae augue vehicula venenatis. Duis elementum id metus vel eleifend. Nam eget magna convallis, gravida magna id, lobortis turpis. Fusce vehicula turpis non neque venenatis, ac feugiat ex blandit. Nullam consequat, libero et tincidunt ullamcorper, libero arcu tincidunt sapien, ut mattis erat odio nec nisl. Ut ac congue risus, in facilisis orci. Nulla in urna et eros ullamcorper vestibulum eget vel mi. Phasellus et quam in nunc interdum eleifend. Aenean molestie, sapien in volutpat viverra, dui enim congue justo, vitae varius turpis ligula id felis. Sed vehicula aliquet quam, ac dapibus lorem pellentesque nec. Sed nec dolor vitae urna tempor tempus non vel magna. Nullam pulvinar sit amet enim eu viverra. Morbi sed dapibus elit.",
        "",
        "Welcome to the Theory page!",
        "",
        "Here you can add your Simulation content.",
        "Use arrow keys to move, space to jump, etc.",
        "",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vitae augue vehicula venenatis. Duis elementum id metus vel eleifend. Nam eget magna convallis, gravida magna id, lobortis turpis. Fusce vehicula turpis non neque venenatis, ac feugiat ex blandit. Nullam consequat, libero et tincidunt ullamcorper, libero arcu tincidunt sapien, ut mattis erat odio nec nisl. Ut ac congue risus, in facilisis orci. Nulla in urna et eros ullamcorper vestibulum eget vel mi. Phasellus et quam in nunc interdum eleifend. Aenean molestie, sapien in volutpat viverra, dui enim congue justo, vitae varius turpis ligula id felis. Sed vehicula aliquet quam, ac dapibus lorem pellentesque nec. Sed nec dolor vitae urna tempor tempus non vel magna. Nullam pulvinar sit amet enim eu viverra. Morbi sed dapibus elit.",
        "",
        "Welcome to the Theory page!",
        "",
        "Here you can add your Simulation content.",
        "Use arrow keys to move, space to jump, etc.",
        "",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac justo vitae augue vehicula venenatis. Duis elementum id metus vel eleifend. Nam eget magna convallis, gravida magna id, lobortis turpis. Fusce vehicula turpis non neque venenatis, ac feugiat ex blandit. Nullam consequat, libero et tincidunt ullamcorper, libero arcu tincidunt sapien, ut mattis erat odio nec nisl. Ut ac congue risus, in facilisis orci. Nulla in urna et eros ullamcorper vestibulum eget vel mi. Phasellus et quam in nunc interdum eleifend. Aenean molestie, sapien in volutpat viverra, dui enim congue justo, vitae varius turpis ligula id felis. Sed vehicula aliquet quam, ac dapibus lorem pellentesque nec. Sed nec dolor vitae urna tempor tempus non vel magna. Nullam pulvinar sit amet enim eu viverra. Morbi sed dapibus elit.",
        "",
        "Press 'Esc' to return to the main menu."
    ]

    
    while running:
        screen.fill(PRIMARY)
        draw_text("Theory", font, TEXT_COLOR, screen_width // 2, 50)

        # Display the Simulation content
        y_offset = 150
        for i, text in enumerate(instruction_text[scroll_pos:]):
            draw_text(text, instruction_font, TEXT_COLOR, screen_width // 2, y_offset)
            y_offset += 30
            if y_offset > screen_height - 30:  # Check if text goes beyond screen
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
                        scroll_pos -= 1  # Decrease scroll position
                elif event.key == pygame.K_DOWN:
                    if scroll_pos < len(instruction_text) - (screen_height - 180) // 30:
                        scroll_pos += 1  # Increase scroll position
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    scroll_pos -= scroll_speed
                elif event.button == 5:  # Scroll down
                    scroll_pos += scroll_speed

# Run the main menu
if __name__ == '__main__':
    main_menu()
