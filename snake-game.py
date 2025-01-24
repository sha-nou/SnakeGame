import pygame
import sys
import random
import time


pygame.init()
# screen settings
screen_width = 720
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

color = (255, 255, 255)
clock = pygame.time.Clock()

# snake_position
snake_position=[100,50]

# fruit position
fruit_position = [                             
    random.randrange(1, (screen_width // 10)) * 10,
    random.randrange(1, (screen_height // 10)) * 10,
]

# snake_body
snake_body = [[100, 50],[90,50],[80,50]]

speed=10
# # initial score
score = 0

direction = "RIGHT"  # Initial direction
change_to = direction  # To change direction


def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    screen.blit(score_surface, score_rect)

def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    
    # blit will draw the text on screen
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# game loop
while True:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update the direction
        direction = change_to

     # Move the snake's head
        if direction == "UP":
          snake_position[1] -= 10
        if direction == "DOWN":
         snake_position[1] += 10
        if direction == "LEFT":
         snake_position[0] -= 10
        if direction == "RIGHT":
         snake_position[0] += 10
   
   
       snake_body.insert(0, list(snake_position))  # Add new head position
       snake_body.pop()  # Remove the last segment for constant length

       for pos in snake_body:
          pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

       pygame.draw.rect(screen,(255,0,0), pygame.Rect(fruit_position[0], fruit_position[1], 10,10))

       pygame.display.flip()
       pygame.display.update()

    # # Detect collision with the wall
    # if snake_position[0] < 0 or snake_position[0] > window_x-10:
    #     game_over()
    # if snake_position[1] < 0 or snake_position[1] > window_y-10:
    #     game_over()

    # # Touching the snake body
    # for block in snake_body[1:]:
    #     if snake_position[0] == block[0] and snake_position[1] == block[1]:
    #         game_over()

