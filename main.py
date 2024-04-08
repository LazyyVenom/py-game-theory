import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prisoner's Dilemma")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
FONT = pygame.font.SysFont(None, 40)

# Define constants
COOPERATE = 'C'
DEFECT = 'D'
TICKS_PER_SECOND = 30
RUNNING = True

# Function to draw text on screen
def draw_text(text, color, x, y):
    text_surface = FONT.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    SCREEN.blit(text_surface, text_rect)

# Function to run the game
def run_game():
    player_decision = None
    ai_decision = random.choice([COOPERATE, DEFECT])
    
    while RUNNING:
        SCREEN.fill(WHITE)
        draw_text("Prisoner's Dilemma", BLACK, WIDTH // 2, 50)
        draw_text("Your decision: Press 'C' to Cooperate, 'D' to Defect", BLACK, WIDTH // 2, 150)
        
        pygame.display.flip()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    player_decision = COOPERATE
                elif event.key == pygame.K_d:
                    player_decision = DEFECT
        
        # Game logic
        if player_decision:
            draw_text(f"Your decision: {player_decision}", BLACK, WIDTH // 2, 250)
            draw_text(f"Opponent's decision: {ai_decision}", BLACK, WIDTH // 2, 300)
            if player_decision == COOPERATE and ai_decision == COOPERATE:
                draw_text("Both Cooperate! Mutual cooperation.", BLACK, WIDTH // 2, 400)
            elif player_decision == COOPERATE and ai_decision == DEFECT:
                draw_text("You Cooperate, Opponent Defects! You lose.", BLACK, WIDTH // 2, 400)
            elif player_decision == DEFECT and ai_decision == COOPERATE:
                draw_text("You Defect, Opponent Cooperates! You win.", BLACK, WIDTH // 2, 400)
            elif player_decision == DEFECT and ai_decision == DEFECT:
                draw_text("Both Defect! Mutual defection.", BLACK, WIDTH // 2, 400)
            
            pygame.display.flip()
            pygame.time.delay(3000)  # Delay for 3 seconds before restarting the game
            
            # Reset decisions for next round
            player_decision = None
            ai_decision = random.choice([COOPERATE, DEFECT])

        pygame.time.Clock().tick(TICKS_PER_SECOND)

if __name__ == "__main__":
    run_game()