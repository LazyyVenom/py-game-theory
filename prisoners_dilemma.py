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
TER_BLUE = (70, 194, 203)
KIND_OF_YELLOW = (242, 247, 161)
BUTTON_BORDER_COLOR = (69, 60, 103)
TEXT_COLOR = SECONDARY
INSTRUCTION_COLOR = SECONDARY
INSTRUCTION_HEADING_COLOR = (242, 247, 161)

# Fonts
font = pygame.font.Font(None, 50)
instruction_font = pygame.font.Font(None, 40)

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
            {"text": "Tournament", "rect": pygame.Rect(screen_width // 2 - 250, 260, 500, 80)},
            {"text": "Simulation", "rect": pygame.Rect(screen_width // 2 - 250, 360, 500, 80)},
            {"text": "Strategies Theory", "rect": pygame.Rect(screen_width // 2 - 250, 460, 500, 80)},
            {"text": "Quit", "rect": pygame.Rect(screen_width // 2 - 250, 560, 500, 80)}
        ]

        for button in buttons:
            if button["rect"].collidepoint((mouse_x, mouse_y)):
                pygame.draw.rect(screen, KIND_OF_YELLOW, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 6) 
            else:
                pygame.draw.rect(screen, TER_BLUE, button["rect"])
                pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button["rect"], 6)  
            draw_text(button["text"], pygame.font.Font(None, 60), TEXT_COLOR, button["rect"].centerx, button["rect"].centery)

        draw_text("Recreation of Axelrod's Tournament by Anubhav Choubey", pygame.font.Font(None, 40), KIND_OF_YELLOW, screen_width//2, 720)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint((mouse_x, mouse_y)):
                        if button["text"] == "Tournament":
                            tournament()

                        elif button["text"] == "Simulation":
                            # Show Simulation
                            print("Starting Simulation")

                        elif button["text"] == "Strategies Theory":
                            show_theory()
          
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
        } for strategy in strategies 
    ]

    while running:
        screen.fill(PRIMARY)
        draw_text("STRATEGY THEORY", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 50)

        y_offset = 100
        for i, strategy in enumerate(instruction_text[scroll_pos:]):
            if scroll_pos % 2 == 0:
                if i % 2 == 0:
                    pygame.draw.rect(screen, TER_BLUE, (50, y_offset, 1100, 200))
                    pygame.draw.rect(screen, SECONDARY, (50, y_offset, 1100, 200),8)

                else:
                    pygame.draw.rect(screen, KIND_OF_YELLOW, (50, y_offset, 1100, 200))
                    pygame.draw.rect(screen, SECONDARY, (50, y_offset, 1100, 200),8)
            
            else:
                if i % 2 != 0:
                    pygame.draw.rect(screen, TER_BLUE, (50, y_offset, 1100, 200))
                    pygame.draw.rect(screen, SECONDARY, (50, y_offset, 1100, 200),8)

                else:
                    pygame.draw.rect(screen, KIND_OF_YELLOW, (50, y_offset, 1100, 200))
                    pygame.draw.rect(screen, SECONDARY, (50, y_offset, 1100, 200),8)

            draw_text(strategy["NAME"],pygame.font.Font(None, 45),(0,0,0),screen_width//2+35,y_offset+50)
            
            desc = strategy["DESCRIPTION"].split("\n")[0].replace("Strategy","").replace(":","").split(" ")
            draw_text(" ".join(desc[:len(desc)//2]),pygame.font.Font(None, 31),SECONDARY,screen_width//2 + 50,y_offset+100)
            draw_text(" ".join(desc[len(desc)//2:]),pygame.font.Font(None, 31),SECONDARY,screen_width//2 + 50,y_offset+140)

            image_path = strategy["IMAGE_PATH"]
            if os.path.exists(image_path):
                image = pygame.image.load(image_path)
                image = pygame.transform.scale(image, (200, 200))
                screen.blit(image, (80, y_offset))
                        
            
            y_offset += 220
            if y_offset > screen_height - 30:
                break

        pygame.draw.rect(screen,SECONDARY,(1100,20,80,50),border_radius=3)
        draw_text("ESC", pygame.font.Font(None,50),PRIMARY,1140, 47)

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
                elif event.button == 1:
                    click_pos = event.pos
                    if (1100 < click_pos[0] < 1180) and (20 < click_pos[1] < 70):
                        running = False
            
            scroll_pos = max(scroll_pos,0)
            scroll_pos = min(scroll_pos,10)

#TO KEEP TRACK OF STRATEGY SELECTION
check_boxes = [True] * len(strategies)

def tournament():
    running = True

    box_dimensions = (550,44)
    box_x = 50
    box_y_initial = 130
    box_y_delta = 52
    box_y_end = box_y_initial + box_y_delta * len(strategies) 

    while running:
        screen.fill(PRIMARY)
        draw_text("TOURNAMENT", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 50)

        paragraph = [
            "Select Strategies,",
            "Select Number Of Rounds,",
            "You Can Read About",
            "Strategies in Theory,",
            "Choose Needed Insights,",
            "And Round Robin Tournament STARTS"
        ]

        pygame.draw.rect(screen,SECONDARY,(630,105,540,250))

        text_y_offset = 130
        for line in paragraph:
            draw_text(line,pygame.font.Font(None,40),(255,255,255),900,text_y_offset)
            
            text_y_offset += 40

        number_of_rounds = ""
        input_selected = False

        draw_text("ROUNDS: ", pygame.font.Font(None,40),(0,0,0),700,400)
        pygame.draw.rect(screen,(255,255,255),(700,420,300,50))

        y_offset = box_y_initial

        for i,strategy in enumerate(strategies):
            if check_boxes[i]:
                pygame.draw.rect(screen, TER_BLUE, (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]))
                pygame.draw.rect(screen,SECONDARY , (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]),3)
                pygame.draw.circle(screen,(40,255,40),(560,y_offset-3),10)
                draw_text(strategy.name, pygame.font.Font(None,40),(255,255,255),325, y_offset-2)

            else:
                pygame.draw.rect(screen, KIND_OF_YELLOW, (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]))
                pygame.draw.rect(screen,SECONDARY , (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]),3)
                pygame.draw.circle(screen,(255,40,40),(560,y_offset-3),10)
                draw_text(strategy.name, pygame.font.Font(None,40),(0,0,0),325, y_offset-2)

            image_path = f"images/{strategy.st_id}.png"
            if os.path.exists(image_path):
                image = pygame.image.load(image_path)
                image = pygame.transform.scale(image, (50, 50))
                screen.blit(image, (80, y_offset - 30))

            y_offset += box_y_delta

        pygame.draw.rect(screen,SECONDARY,(1100,20,80,50),border_radius=3)
        draw_text("ESC", pygame.font.Font(None,50),PRIMARY,1140, 47)


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_pos = event.pos

                    if (1100 < click_pos[0] < 1180) and (20 < click_pos[1] < 70):
                        running = False
                    
                    elif () and ():
                        input_selected = not input_selected

                    x_range = (box_x,box_x+box_dimensions[0])

                    i_count = 0
                    for y in range(box_y_initial+10,box_y_end + 1,box_y_delta):
                        if x_range[0] < click_pos[0] < x_range[1]:
                            if y - box_y_delta < click_pos[1] < y:
                                check_boxes[i_count] = not check_boxes[i_count]
                    
                        i_count += 1


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if input_selected:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode


if __name__ == '__main__':
    main_menu()