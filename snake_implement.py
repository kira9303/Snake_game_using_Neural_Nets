import pygame
import time
import random
import sys
import pickle
import numpy as np

from keras.models import load_model
model = load_model('snake_train.h5')

#input format for model = (foodx, foody, x1, y1)
 
pygame.init()

direction = ["up", "down", "left", "right"]

training_data = []
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 500
dis_height = 500
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10

pre_direction = "up"
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
    
    current_direction = "up"
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        #print("x and y of snake are: {}".format(x1, y1))
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pickle.dump(training_data,open('training_data.pkl','wb'))
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT:
                    #current_direction = "left"
                    
                    #x1_change = -snake_block
                    #y1_change = 0
                #elif event.key == pygame.K_RIGHT:
                    #current_direction = "right"
                    
                    #x1_change = snake_block
                    #y1_change = 0
                #elif event.key == pygame.K_UP:
                    #current_direction = "up"
                    
                   # y1_change = -snake_block
                    #x1_change = 0
                #elif event.key == pygame.K_DOWN:
                    #current_direction = "down"
                    
                    #y1_change = snake_block
                    #x1_change = 0
        new_foodx = foodx
        new_foody = foody
        new_x1 = x1
        new_y1 = y1
        first_pred = [new_foodx, new_foody, new_x1, new_y1]
        first_pred = np.array(first_pred)
        first_pred = first_pred.reshape(-1, 4)
        #first_pred = first_pred / 500.0
        print(first_pred[0]/500.0)
        #first_pred.reshape(-1, 4)
        first_pred[0] = first_pred[0] / 500.0
        prediction = model.predict(first_pred)
        new_input = []
        new_input.append(float(foodx)/500.0)
        new_input.append(float(foody)/500.0)
        new_input.append(float(x1)/500.0)
        new_input.append(float(y1)/500.0)
        #print("new input is: {}".format(new_input))
       # print("shape of new_input is: {}".format(np.shape(new_input)))
        #prediction = model.predict([[foodx, foody, x1, y1]])
        print("prediction is:  {}".format(np.round(prediction[0])))
        for i in range(0, len(prediction[0])):
            if(i==0):
                if(np.round(prediction[0][i])==1):      #left
                    current_direction = "left"
                    y1_change = -snake_block
                    x1_change = 0
            if(i==1):
                if(np.round(prediction[0][i])==1):      #right
                    current_direction = "right"
                    y1_change = snake_block
                    x1_change = 0
                   
            if(i==2):
                if(np.round(prediction[0][i])==1):      #up
                    current_direction = "up"
                    x1_change = -snake_block
                    y1_change = 0
                        
            if(i==3):
                if(np.round(prediction[0][i])==1):     #down
                    current_direction = "down"
                    x1_change = snake_block
                    y1_change = 0
                        
                    
                    
            
                    
                    
                    
        
    
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        #for x in snake_List[:-1]:
            #if x == snake_Head:
                #game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        
       # print("x and y of snake are: {}, {}".format(x1, y1))
        #pre_direction = current_direction
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    sys.exit()
    
#training_data.append(1)

    
#pickle.dump(training_data,open('training_data.pkl','wb'))

#print("training data required is: {}".format(training_data))

#print("shape of the training data is {}".format(np.shape(training_data)))

 
 
gameLoop()