import random
class Ball:
    def __init__(self, width, height):
        self.ballX, self.ballY = width/2, height/2
        self.ballWidth, self.ballheight = 10, 10
        self.ballDirX, self.ballDirY = random.uniform(-1,1), 1
    
    def frameMove(self):
        
        self.ballX = self.ballX+ self.ballDirX*5
        self.ballY = self.ballY+ self.ballDirY*5

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