import pygame, sys

def cursor(screen,x,y):
    pygame.draw.ellipse(screen, white, [x - 10, y - 10, 20, 20], 0)


pygame.init()

baseSpeed = 20

size = width, height = 1500, 1500
speed = [0, 0]
black = (0, 0, 0)
white = (255,255,255)

#############

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/ball.gif")
ballrect = ball.get_rect()

gameover = False


while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = -baseSpeed
            elif event.key == pygame.K_RIGHT:
                speed[0] = baseSpeed
            elif event.key == pygame.K_DOWN:
                speed[1] = baseSpeed
            elif event.key == pygame.K_UP:
                speed[1] = -baseSpeed


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed[0] = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed[1] = 0



    screen.fill(black)

    pos = pygame.mouse.get_pos()

    posX = pos[0]
    posY = pos[1]

    cursor(screen, posX, posY)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = 0
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = 0


    screen.blit(ball, ballrect)
    pygame.display.flip()
