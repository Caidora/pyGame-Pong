import random
class Ball:
    def __init__(self, width, height, speed=5):
        self.ballX, self.ballY, self.speed= width/2, 0+(height/10), speed
        self.ballWidth, self.ballheight = 10, 10
        self.ballDirX, self.ballDirY = random.uniform(-1,1), 1
    
    def frameMove(self):
        
        self.ballX = self.ballX+ self.ballDirX*self.speed
        self.ballY = self.ballY+ self.ballDirY*self.speed

    def getX(self):
        return(self.ballX)

    def getY(self):
        return(self.ballY)

    def getWidth(self):
        return(self.ballWidth)
    
    def getHeight(self):
        return(self.ballheight)
    
    def collide(self):
        self.ballDirY = self.ballDirY * -1
        self.ballDirX = random.uniform(-1, 1)*-1
    
    def collideX(self):
        self.ballDirX = self.ballDirX * -1