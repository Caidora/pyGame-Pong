from curses.textpad import rectangle
import sys, pygame
import random 
from Ball import Ball
random.seed()
pygame.init()
clock = pygame.time.Clock()
black = 0,0,0
white = 255,255,255
size = width, height = 1600, 1200
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('arial', 300)


paddleHeight, paddleWidth = 25, 200
playerX, playerY = width/2-(paddleWidth/2), height-35
enemyX, enemyY = width/2-(paddleWidth/2), 10
player = pygame.Rect(playerX, playerY, paddleWidth, paddleHeight)
enemy = pygame.Rect(enemyX, enemyY, paddleWidth, paddleHeight)

ingame = True
p1Score = 0
p2Score = 0
run = 1
ball = False
while ingame:
    clock.tick(165)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if(ball == False):
        currentBall = Ball(width, height)
        ball = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x>10:
        player.x -=5
    if keys[pygame.K_RIGHT] and player.x<width-paddleWidth-10:
        player.x +=5
    if keys[pygame.K_a] and enemy.x>10:
        enemy.x -=5
    if keys[pygame.K_d] and enemy.x<width-paddleWidth-10:
        enemy.x +=5

    currentBall.frameMove()

    if(currentBall.getY()>height-currentBall.getWidth()-paddleHeight-10):
        if(currentBall.getX()>player.x and currentBall.getX()<player.x+paddleWidth):
            currentBall.collide()
        else:
            ball = False
            p2Score +=1
    elif(currentBall.getY()<0+currentBall.getWidth()+paddleHeight+10):
        if(currentBall.getX()>enemy.x and currentBall.getX()<enemy.x+paddleWidth):
            currentBall.collide()
        else:
            ball = False
            p1Score +=1
    if((currentBall.getX()>width-currentBall.getWidth()) or (currentBall.getX()<0+currentBall.getWidth())):
        currentBall.collideX()
    
    screen.fill(black)

    letterPlayer = font.render(str(p1Score),True, white)
    letterEnemy = font.render(str(p2Score),True, white)
    screen.blit(letterEnemy, ((3*width)/4,height/2-letterPlayer.get_height()/2))
    screen.blit(letterPlayer, (width/4-letterPlayer.get_width(),height/2-letterPlayer.get_height()/2))

    pygame.draw.circle(screen, white, (currentBall.getX(), currentBall.getY()), currentBall.getWidth(), 0)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, enemy)
    pygame.display.update()


        

    
        
