from curses.textpad import rectangle
import sys, pygame
import random 
random.seed()
pygame.init()
clock = pygame.time.Clock()
black = 0,0,0
white = 255,255,255
size = width, height = 1600, 1200
screen = pygame.display.set_mode(size)

ballX, ballY = width/2, height/2
ballWidth, ballheight = 10, 10
ballDirX, ballDirY = -1, 1 

paddleHeight, paddleWidth = 25, 200
playerX, playerY = width/2-(paddleWidth/2), height-35
enemyX, enemyY = width/2-(paddleWidth/2), 10
player = pygame.Rect(playerX, playerY, paddleWidth, paddleHeight)
enemy = pygame.Rect(enemyX, enemyY, paddleWidth, paddleHeight)

ingame = True
p1Score = 0
p2Score = 0
run = 1
Ball = False
while ingame:
    clock.tick(165)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    if(Ball == False):
        Ball = True
        currentBallX, currentBallY, currentBallDirX, currentBallDirY = ballX, ballY, ballDirX, ballDirY


        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x>10:
        player.x -=5
    if keys[pygame.K_RIGHT] and player.x<width-paddleWidth-10:
        player.x +=5
    if keys[pygame.K_a] and enemy.x>10:
        enemy.x -=5
    if keys[pygame.K_d] and enemy.x<width-paddleWidth-10:
        enemy.x +=5

    currentBallX = currentBallX+ currentBallDirX*3
    currentBallY = currentBallY+ currentBallDirY*3
    print(currentBallY)

    if(currentBallY>height-ballWidth-paddleHeight-10):
        if(currentBallX>player.x and currentBallX<player.x+paddleWidth):
            currentBallDirY = currentBallDirY * -1
            currentBallDirX = random.uniform(-1, 1)*-1
        else:
            Ball = False
            p2Score +=1
    elif(currentBallY<0+ballWidth+paddleHeight+10):
        if(currentBallX>enemy.x and currentBallX<enemy.x+paddleWidth):
            currentBallDirY = currentBallDirY * -1
            currentBallDirX = random.uniform(-1, 1)*-1
        else:
            Ball = False
            p1Score +=1
    if((currentBallX>width-ballWidth) or (currentBallX<0+ballWidth)):
        currentBallDirX = currentBallDirX * -1
    screen.fill(black)
    pygame.draw.circle(screen, white, (currentBallX, currentBallY), ballWidth, 0)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, enemy)
    pygame.display.update()
    if(run==0):
        pygame.quit()
        exit()

    
        
