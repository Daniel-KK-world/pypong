#Game Modules
import pygame
from pygame import *

#let's initialize
pygame.init()

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

#displaying the window res 500 by 400 basically parameters
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Now we have to give our window a name. 
pygame.display.set_caption('PyPong')
#Handling our frame rate. 
clock = pygame.time.Clock()
FPS = 30

#Creating a player class that handles the player and all related objects.
class Striler:
    #Now we take the initial position, speed and color of the object 
    def __init__(self, posx, posy, speed, width, height, color ):
        self.posx = posx
        self.posy = posy 
        self.width = width 
        self.height = height 
        self.speed = speed 
        self.color = color 
        #Rectangle to handle collision and obj pos. 
        self.danRect = pygame.Rect(posx, posy, width, height )
        #object on the screen 
        self.dan = pygame.draw.rect(screen, self.color, self.danRect)
    
    #Now we have to display objects
    def display(self):
        self.dan = pygame.draw.rect(screen, self.color, self.danRect)
    #now we have to be updating everything that happens to the screen. we can think of it like how we say videos are moving pictures so we would be updating the screen constatly with these pictures or instances if u like. 
    #yFac is the direction of the striker movement
    #If yFac == -1 ==> the object is moving upward 
    #if yFac == 1 ==> the object is moving downareds 
    #And if it's zero the object is not moving. 
    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac
        
        #Restricting the striker to be below top surface of screen 
        if self.posy <= 0:
            self.posy = 0
        #Restrictiong again the striker to be above the bottom of the screen 
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height 
        #Updating the rect with new values 
        self.danRect = (self.posx, self.posy, self.width, self.height)
        
    #rendering the score on the screen
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+ str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        
        screen.bilt(text, textRect)
        
    def rect(self):
        return self.danRect
    
#Ball class 
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx 
        self.posy = posy 
        self.radius = radius 
        self.speed = speed 
        self.color = color 
        self.xFax = 1
        self.yfac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius
        )
        self.firstTime = 1 
        
    def display(self):
        self.ball = pygame.draw.circle( 
                                       screen, self.color, (self.posx, self.posy), self.radius
                                       )
        
    def update(self):
        self.posx += self.speed * self.xFac 
        self.posy += self.speed * self.yFac
          # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and it
        # results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1 
         # If the ball touches the left wall for the first time,
        # The firstTime is set to 0 and we return 1
        # indicating that Geek2 has scored
        # firstTime is set to 0 so that the condition is
        # met only once and we can avoid giving multiple
        # points to the player
        if self.posx <= 0 and self.firstTime: 
            self.firstTime = 0 
            return -1
        else: 
            return 0 
        # Used to reset the position of the ball
        # to the center of the screen
    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.xFac *= -1
        self.firstTime = 1
        
        # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
        
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
        
    
    #Game Manager. 
    def main():
        running = True
        
        





#Declaring my boolean that checks if pypong is runnig.
#keepGameRunnig = True

#while keepGameRunnig:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #keepGameRunnig = False



