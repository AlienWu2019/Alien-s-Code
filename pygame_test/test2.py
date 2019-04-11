import pygame_test
import time
import random

pygame_test.init()

white = (255,255,255)
black = (0,0,0,)
red = (255,0,0)
green = (0,255,0)

display_width = 800
display_heigth = 600

gamedisplay = pygame_test.display.set_mode((display_width, display_heigth))
pygame_test.display.set_caption('Slither')


clock = pygame_test.time.Clock()

font = pygame_test.font.SysFont('arial', 25)

def snake(block_size,snakelist):
    for XnY in snakelist:
        pygame_test.draw.rect(gamedisplay, green, [XnY[0], XnY[1], block_size, block_size])

def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gamedisplay.blit(screen_text,[display_width/4,display_heigth/2])

def gameLoop():
    gameExit = False
    gameOver = False
    block_size = 10

    lead_x = display_width/2
    lead_y = display_heigth/2

    lead_x_change = 0
    lead_y_change = 0

    randAppleX = random.randrange(0,display_width-block_size)
    randAppleY = random.randrange(0,display_heigth-block_size)

    while not gameExit:

        while gameOver == True:
            gamedisplay.fill(white)
            message_to_screen("Game over,press C to play again or Q to quit",red)
            pygame_test.display.update()

            for event in pygame_test.event.get():
                if event.type == pygame_test.KEYDOWN:
                    if event.key == pygame_test.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame_test.K_c:
                        gameLoop()

        for event in pygame_test.event.get():
            if event.type == pygame_test.QUIT:
                gameExit = True
            if event.type == pygame_test.KEYDOWN:
                if event.key == pygame_test.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame_test.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame_test.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame_test.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x > display_width or lead_x <0 or lead_y > display_heigth or lead_y < 0:
            gameOver = True

        gamedisplay.fill(white)
        pygame_test.draw.rect(gamedisplay, red, [randAppleX, randAppleY, block_size, block_size])
        snakelist = []
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)
        snake(block_size,snakelist)

        pygame_test.display.update()

        clock.tick(30)

    pygame_test.quit()
    quit()

gameLoop()
