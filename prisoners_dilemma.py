import pygame
import sys
from strategy import strategies, Strategy, score
import random
import typing
from main import tournament_logic
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
FONT_SIZE = 40
INSTRUCTION_COLOR = SECONDARY
INSTRUCTION_HEADING_COLOR = (242, 247, 161)

# Fonts
font = pygame.font.Font(None, 40)
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
                            simulation()

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
    number_of_rounds = ""
    input_selected = False
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
            "Tournament Is Round Robin Based",
            "(Including Self With Self)",
            "Both Cooperate - 3pts to both",
            "Both Defect - 1pts to both",
            "One Defects - 5pts to Defect",
            "0pts To Cooperate"
        ]

        pygame.draw.rect(screen,SECONDARY,(630,105,540,405))
        pygame.draw.rect(screen,(255,255,255),(630,105,540,405),3)

        text_y_offset = 130
        for line in paragraph[:6]:
            draw_text(line,pygame.font.Font(None,40),(255,255,255),900,text_y_offset)
            
            text_y_offset += 40

        for line in paragraph[6:]:
            draw_text(line,pygame.font.Font(None,40),TER_BLUE,900,text_y_offset)
            
            text_y_offset += 40

        draw_text("ROUNDS: ", pygame.font.Font(None,40),SECONDARY,701,590)
        pygame.draw.rect(screen,(255,255,255),(770,564,400,50))
        if input_selected:
            pygame.draw.rect(screen,SECONDARY,(770,564,400,50),5)
        
        else:
            pygame.draw.rect(screen,PRIMARY,(770,564,400,50),5)

        text_surface = font.render(number_of_rounds, True, SECONDARY)
        screen.blit(text_surface, (776, 573))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if (630 < mouse_x < 1180) and (670 < mouse_y < 720):
            pygame.draw.rect(screen,KIND_OF_YELLOW,(630,670,540,50))
            pygame.draw.rect(screen,SECONDARY,(630,670,540,50),5)
            draw_text("START",pygame.font.Font(None,57),SECONDARY,900,695)
        else:
            pygame.draw.rect(screen,SECONDARY,(630,670,540,50))
            pygame.draw.rect(screen,KIND_OF_YELLOW,(630,670,540,50),5)
            draw_text("START",pygame.font.Font(None,57),KIND_OF_YELLOW,900,695)

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
                    
                    elif (770 < click_pos[0] < 1170) and (554 < click_pos[1] < 604):
                        input_selected = True
                    
                    elif (630 < click_pos[0] < 1180) and (670 < click_pos[1] < 720):
                        try:
                            tournament_start(check_boxes,strategies,int(number_of_rounds))
                        except Exception as e:
                            print(f"Error: {e}")

                    else:
                        input_selected = False

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
                       number_of_rounds =number_of_rounds[:-1]
                    else:
                       ch = event.unicode

                       if ch in "0123456789":
                            number_of_rounds += event.unicode


def simulation():
    running = True
    input_selected = [False] * len(strategies)
    inputs = ["50"] * len(strategies)
    input_dimensions = (100,44)
    box_dimensions = (500,44)
    box_x = 50
    box_y_initial = 130
    box_y_delta = 52
    box_y_end = box_y_initial + box_y_delta * len(strategies) 

    while running:
        screen.fill(PRIMARY)
        draw_text("SIMULATION", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 50)

        paragraph = [
            "Select Strategies,",
            "Select Number Of People,",
            "You Can Read About",
            "Strategies in Theory,",
            "Tournament Is Round Robin Based",
            "(Including Self With Self)",
            "Both Cooperate - 3pts to both",
            "Both Defect - 1pts to both",
            "One Defects - 5pts to Defect",
            "0pts To Cooperate"
        ]

        pygame.draw.rect(screen,SECONDARY,(680,105,490,405))
        pygame.draw.rect(screen,(255,255,255),(680,105,490,405),2)

        text_y_offset = 130
        for line in paragraph[:6]:
            draw_text(line,pygame.font.Font(None,40),(255,255,255),925,text_y_offset)
            
            text_y_offset += 40

        for line in paragraph[6:]:
            draw_text(line,pygame.font.Font(None,40),TER_BLUE,925,text_y_offset)
            
            text_y_offset += 40

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if (680 < mouse_x < 1180) and (670 < mouse_y < 720):
            pygame.draw.rect(screen,KIND_OF_YELLOW,(680,670,490,50))
            pygame.draw.rect(screen,SECONDARY,(680,670,490,50),5)
            draw_text("START",pygame.font.Font(None,57),SECONDARY,925,695)
        else:
            pygame.draw.rect(screen,SECONDARY,(680,670,490,50))
            pygame.draw.rect(screen,KIND_OF_YELLOW,(680,670,490,50),5)
            draw_text("START",pygame.font.Font(None,57),KIND_OF_YELLOW,925,695)

        y_offset = box_y_initial

        for i,strategy in enumerate(strategies):
            if check_boxes[i]:
                pygame.draw.rect(screen, TER_BLUE, (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]))
                pygame.draw.rect(screen,SECONDARY , (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]),3)
                pygame.draw.rect(screen,SECONDARY , (box_x + 510, y_offset-25, input_dimensions[0], input_dimensions[1]))

                if input_selected[i]:
                    pygame.draw.rect(screen,(255,255,255), (box_x + 510, y_offset-25, input_dimensions[0], input_dimensions[1]),2)
                
                pygame.draw.circle(screen,(40,255,40),(520,y_offset-3),10)
                draw_text(strategy.name, pygame.font.Font(None,40),(255,255,255),325, y_offset-2)

                text_surface = font.render(inputs[i], True, (255,255,255))
                screen.blit(text_surface, (570, y_offset-15))

            else:
                pygame.draw.rect(screen, KIND_OF_YELLOW, (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]))
                pygame.draw.rect(screen,SECONDARY , (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]),3)
                # pygame.draw.rect(screen,SECONDARY , (box_x + 510, y_offset-25, input_dimensions[0], input_dimensions[1]))
                
                pygame.draw.circle(screen,(255,40,40),(520,y_offset-3),10)
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
                    
                    elif (630 < click_pos[0] < 1180) and (670 < click_pos[1] < 720):
                        # try:
                        simulation_start(strategies,check_boxes,inputs)
                        # except Exception as e:
                        #     print(f"Error: {e}")

                    else:
                        input_selected = [False] * len(strategies)

                    x_range = (box_x,box_x+box_dimensions[0])

                    i_count = 0
                    for y in range(box_y_initial+10,box_y_end + 1,box_y_delta):
                        if x_range[0] < click_pos[0] < x_range[1]:
                            if y - box_y_delta < click_pos[1] < y:
                                check_boxes[i_count] = not check_boxes[i_count]
                    
                        i_count += 1

                    i_count = 0
                    for y in range(box_y_initial+10,box_y_end + 1,box_y_delta):
                        if 580 < click_pos[0] < 680:
                            if y - box_y_delta < click_pos[1] < y:
                                input_selected[i_count] = not input_selected[i_count]
                                break
                    
                        i_count += 1

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if True in input_selected:
                    needed_index = input_selected.index(True)

                    if event.key == pygame.K_BACKSPACE:
                       inputs[needed_index] = inputs[needed_index][:-1]
                    else:
                       ch = event.unicode

                       if ch in "0123456789":
                            inputs[needed_index] += event.unicode


def tournament_start(flags: list, strategies: typing.List[Strategy], rounds: int) -> None:
    needed_strategies = []
    for i in range(len(strategies)):
        if flags[i]:
            needed_strategies.append(strategies[i])

    print("STARTING THE TOURNAMENT")
    scores = tournament_logic(needed_strategies,rounds)
    
    display_data = []
    for i in range(len(scores)):
        display_data.append([needed_strategies[i],scores[i]])
    
    display_data.sort(key= lambda x: x[1][0],reverse=True)


    running = True

    while running:
        screen.fill(PRIMARY)
        draw_text("TOURNAMENT RESULT", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 50)

        box_dimensions = (500,44)
        score_box_dimensions = (100,44)
        box_x = 50
        box_y_initial = 180
        y_offset = box_y_initial
        box_y_delta = 48
        if display_data[0][1][0] == 0:
            running = False

        per_point_value = (box_dimensions[0]/display_data[0][1][0]) * 0.95

        pygame.draw.rect(screen, TER_BLUE, (box_x, 105, box_dimensions[0], box_dimensions[1]))
        pygame.draw.rect(screen,SECONDARY , (box_x, 105, box_dimensions[0], box_dimensions[1]),3)
        draw_text("Strategy Name", pygame.font.Font(None,40),(250,250,250),300, 130-2)
        
        pygame.draw.rect(screen, TER_BLUE, (555, 105, score_box_dimensions[0], score_box_dimensions[1]))
        pygame.draw.rect(screen,SECONDARY , (555, 105, score_box_dimensions[0], score_box_dimensions[1]),3)
        draw_text("Score", pygame.font.Font(None,40),(250,250,250),605, 130-2)

        pygame.draw.rect(screen, TER_BLUE, (665, 105, score_box_dimensions[0], score_box_dimensions[1]))
        pygame.draw.rect(screen,SECONDARY , (665, 105, score_box_dimensions[0], score_box_dimensions[1]),3)
        draw_text("5 Pts", pygame.font.Font(None,40),(250,250,250),715, 130-2)

        pygame.draw.rect(screen, TER_BLUE, (775, 105, score_box_dimensions[0], score_box_dimensions[1]))
        pygame.draw.rect(screen,SECONDARY , (775, 105, score_box_dimensions[0], score_box_dimensions[1]),3)
        draw_text("3 Pts", pygame.font.Font(None,40),(250,250,250),825, 130-2)

        pygame.draw.rect(screen, TER_BLUE, (885, 105, score_box_dimensions[0], score_box_dimensions[1]))
        pygame.draw.rect(screen,SECONDARY , (885, 105, score_box_dimensions[0], score_box_dimensions[1]),3)
        draw_text("1 Pts", pygame.font.Font(None,40),(250,250,250),935, 130-2)

        pygame.draw.rect(screen, TER_BLUE, (995, 105, score_box_dimensions[0], score_box_dimensions[1]))
        pygame.draw.rect(screen,SECONDARY , (995, 105, score_box_dimensions[0], score_box_dimensions[1]),3)
        draw_text("0 Pts", pygame.font.Font(None,40),(250,250,250),1045, 130-2)
        
        for data in display_data:
            strategy_color = (55,200,55) if data[0].strategy_type == "NICE" else (200,55,55)

            pygame.draw.rect(screen, KIND_OF_YELLOW, (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]))

            pygame.draw.rect(screen, strategy_color, (box_x, y_offset-25, int(data[1][0]*per_point_value), box_dimensions[1]))

            pygame.draw.rect(screen,SECONDARY , (box_x, y_offset-25, box_dimensions[0], box_dimensions[1]),3)
            draw_text(data[0].name, pygame.font.Font(None,40),(50,50,50),325, y_offset-2)
            
            pygame.draw.rect(screen, KIND_OF_YELLOW, (555, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]))
            pygame.draw.rect(screen,SECONDARY , (555, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]),3)
            draw_text(str(data[1][0]), pygame.font.Font(None,40),(50,50,50),605, y_offset-2)

            pygame.draw.rect(screen, KIND_OF_YELLOW, (665, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]))
            pygame.draw.rect(screen,SECONDARY , (665, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]),3)
            draw_text(str(data[1][4]), pygame.font.Font(None,40),(50,50,50),715, y_offset-2)

            pygame.draw.rect(screen, KIND_OF_YELLOW, (775, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]))
            pygame.draw.rect(screen,SECONDARY , (775, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]),3)
            draw_text(str(data[1][3]), pygame.font.Font(None,40),(50,50,50),825, y_offset-2)

            pygame.draw.rect(screen, KIND_OF_YELLOW, (885, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]))
            pygame.draw.rect(screen,SECONDARY , (885, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]),3)
            draw_text(str(data[1][2]), pygame.font.Font(None,40),(50,50,50),935, y_offset-2)

            pygame.draw.rect(screen, KIND_OF_YELLOW, (995, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]))
            pygame.draw.rect(screen,SECONDARY , (995, y_offset-25, score_box_dimensions[0], score_box_dimensions[1]),3)
            draw_text(str(data[1][1]), pygame.font.Font(None,40),(50,50,50),1045, y_offset-2)

            image_path = f"images/{data[0].st_id}.png"

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    return 


def display_simulation_data(display_data):
    box_dimensions = (500, 44)
    score_box_dimensions = (100, 44)
    box_x = 50
    box_y_initial = 180
    y_offset = box_y_initial
    box_y_delta = 48

    max_alive = max(data[1] for data in display_data)
    if max_alive == 0:
        per_point_value = 0
        
    else:
        per_point_value = (box_dimensions[0] / max_alive) * 0.95

    pygame.draw.rect(screen, TER_BLUE, (box_x, 105, box_dimensions[0], box_dimensions[1]))
    pygame.draw.rect(screen, SECONDARY, (box_x, 105, box_dimensions[0], box_dimensions[1]), 3)
    draw_text("Strategy Name", pygame.font.Font(None, FONT_SIZE), (250, 250, 250), 300, 130 - 2)

    for data in display_data:
        strategy_color = (55, 200, 55) if data[0].strategy_type == "NICE" else (200, 55, 55)
        pygame.draw.rect(screen, KIND_OF_YELLOW, (box_x, y_offset - 25, box_dimensions[0], box_dimensions[1]))
        pygame.draw.rect(screen, strategy_color, (box_x, y_offset - 25, int(data[1] * per_point_value), box_dimensions[1]))
        pygame.draw.rect(screen, SECONDARY, (box_x, y_offset - 25, box_dimensions[0], box_dimensions[1]), 3)
        draw_text(data[0].name, pygame.font.Font(None, FONT_SIZE), (50, 50, 50), 325, y_offset - 2)

        for i in range(5):
            x_pos = 555 + i * 110
            pygame.draw.rect(screen, KIND_OF_YELLOW, (x_pos, y_offset - 25, score_box_dimensions[0], score_box_dimensions[1]))
            pygame.draw.rect(screen, SECONDARY, (x_pos, y_offset - 25, score_box_dimensions[0], score_box_dimensions[1]), 3)
            draw_text(str(data[1]), pygame.font.Font(None, FONT_SIZE), (50, 50, 50), x_pos + 50, y_offset - 2)

        image_path = f"images/{data[0].st_id}.png"
        if os.path.exists(image_path):
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (50, 50))
            screen.blit(image, (80, y_offset - 30))

        y_offset += box_y_delta

# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos = event.pos
                if (1100 < click_pos[0] < 1180) and (20 < click_pos[1] < 70):
                    return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def simulate_interactions(alive_strategies):
    for i in range(len(alive_strategies)):
        if alive_strategies[i][1] > 0:
            alive_strategies[i][1] -= 1 if (alive_strategies[i][1] > 0 and random.random() < 0.1) else 0

def simulation_start(strategies, flags, inputs):
    needed_strategies = [strategies[i] for i in range(len(strategies)) if flags[i]]

    print("STARTING THE SIMULATION")

    display_data = [[needed_strategies[i], int(inputs[i])] for i in range(len(inputs))]
    running = True
    prev_results = []

    while running:
        screen.fill(PRIMARY)
        draw_text("SIMULATION RUNNING", pygame.font.Font(None, 80), TEXT_COLOR, screen_width // 2, 50)

        if display_data[0][1] == 0:
            running = False

        display_simulation_data(display_data)

        pygame.draw.rect(screen, SECONDARY, (1100, 20, 80, 50), border_radius=3)
        draw_text("ESC", pygame.font.Font(None, 50), PRIMARY, 1140, 47)

        pygame.display.update()

        running = handle_events()

        # Update the simulation logic
        simulate_interactions(display_data)
        prev_results.append([data[1] for data in display_data])

    return

if __name__ == '__main__':
    main_menu()