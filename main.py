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
    def displayScore():
        pass
        





#Declaring my boolean that checks if pypong is runnig.
keepGameRunnig = True

while keepGameRunnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGameRunnig = False



