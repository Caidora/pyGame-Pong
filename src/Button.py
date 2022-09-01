import pygame
class Button:

    def __init__(self, screen, x, y, text = "Button", buttonWidth = 140, buttonHeight = 40):
        self.width, self.height = screen.get_size()
        self.x = x
        self.y = y
        self.adjustedX = x-(buttonWidth/2)
        self.adjustedY = y-(buttonHeight/2)
        self.screen = screen
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.text = text
        self.font = pygame.font.SysFont('arial', self.buttonHeight)
    
    def draw(self, mouse):
        white = 255,255,255
        darker = 100,100,100
        if self.adjustedX <= mouse[0] <= self.adjustedX+self.buttonWidth and self.adjustedY <= mouse[1] <= self.adjustedY+self.buttonHeight:
            pygame.draw.rect(self.screen,white,[self.adjustedX,self.adjustedY,self.buttonWidth,self.buttonHeight])
            self.renderText(darker)
          
        else:
            pygame.draw.rect(self.screen,darker,[self.adjustedX,self.adjustedY,self.buttonWidth,self.buttonHeight])
            self.renderText(white)
            
    def renderText(self, color):
        renderedText = self.font.render(self.text, True, color)
        self.screen.blit(renderedText, ((self.adjustedX+(self.buttonWidth-renderedText.get_width())/2), self.adjustedY))

    def pressed(self, mouse):
        if self.adjustedX <= mouse[0] <= self.adjustedX+self.buttonWidth and self.adjustedY <= mouse[1] <= self.adjustedY+self.buttonHeight:
            return(True)
    
    def getButtonWidth(self):
        return(self.buttonWidth)
        
    def getButtonHeight(self):
        return(self.buttonHeight)

    def getX(self):
        return(self.adjustedX)
        
    def getY(self):
        return(self.adjustedY)
