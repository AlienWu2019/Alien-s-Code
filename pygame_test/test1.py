import sys,pygame_test
pygame_test.init()

size = width,height =600,800
speed = [2,2]
black = 0,0,0

screen =pygame_test.display.set_mode(size)

ball = pygame_test.image.load("D:/test/test.jpg")
ballrect = ball.get_rect()

while 1:
    for event in pygame_test.event.get():
        if event.type == pygame_test.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left<0 or ballrect.right >width:
        speed[0] = -speed[0]
    if ballrect.top <0 or ballrect.bottom >height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball,ballrect)
    pygame_test.display.flip()
