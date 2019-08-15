# Fig. 24.6: fig24_06.py
# Space Cruiser game using pygame.

import os
import sys
import random
import pygame, pygame.image, pygame.font, pygame.mixer
from pygame.locals import *

class Sprite:
   """An object to place on the screen"""

   def __init__( self, image ):
      """Initialize object image and calculate rectangle"""
      
      self.image = image
      self.rectangle = image.get_rect()

   def place( self, screen ):
      """Place object on the screen"""
      
      return screen.blit( self.image, self.rectangle )

   def remove( self, screen, background ):
      """Place background over image to remove it"""
      
      return screen.blit( background, self.rectangle,
         self.rectangle )

class Player( Sprite ):
   """Player Sprite with 4 different states"""

   def __init__( self, images, crashImage,
      centerX = 0, centerY = 0 ):
      """Store images and set initial Player state"""
      
      self.movingImages = images
      self.crashImage = crashImage
      self.centerX = centerX
      self.centerY = centerY
      self.playerPosition = 1   # start player facing down
      self.speed = 0
      self.loadImage()

   def loadImage( self ):
      """Load Player image and calculate rectangle"""

      if self.playerPosition == -1:   # player has crashed
         image = self.crashImage        
      else:
         image = self.movingImages[ self.playerPosition ]

      Sprite.__init__( self, image )
      self.rectangle.centerx = self.centerX
      self.rectangle.centery = self.centerY

   def moveLeft( self ):
      """Change Player image to face one position to left"""

      if self.playerPosition == -1:   # player crashed
         self.speed = 1
         self.playerPosition = 0      # move left of obstacle
      elif self.playerPosition > 0:
         self.playerPosition -= 1

      self.loadImage()

   def moveRight( self ):
      """Change Player image to face one position to right"""

      if self.playerPosition == -1:   # player crashed
         self.speed = 1
         self.playerPosition = 2      # move right of obstacle
      elif self.playerPosition < ( len( self.movingImages ) - 1 ):
         self.playerPosition += 1

      self.loadImage()

   def decreaseSpeed( self ):

      if self.speed > 0:
         self.speed -= 1

   def increaseSpeed( self ):

      if self.speed < 10:      
         self.speed += 1

      # player crashed, start player facing down
      if self.playerPosition == -1:
         self.playerPosition = 1
         self.loadImage()

   def collision( self ):
      """Change Player image to crashed player"""

      self.speed = 0   
      self.playerPosition = -1
      self.loadImage()

   def collisionBox( self ):
      """Return smaller bounding box for collision tests"""
      
      return self.rectangle.inflate( -20, -20 )

   def isMoving( self ):
      """Player is not moving if speed is 0"""

      if self.speed == 0:
         return 0
      else:
         return 1
      
   def distanceMoved( self ):
      """Player moves twice as fast when facing straight down"""

      xIncrement, yIncrement = 0, 0      

      if self.isMoving():

         if self.playerPosition == 1:
            xIncrement = 0
            yIncrement = 2 * self.speed
         else:
            xIncrement = ( self.playerPosition - 1 ) * self.speed
            yIncrement = self.speed

      return xIncrement, yIncrement

class Obstacle( Sprite ):
   """Moveable Obstacle Sprite"""

   def __init__( self, image, centerX = 0, centerY = 0 ):
      """Load Obstacle image and initialize rectangle"""
      
      Sprite.__init__( self, image )

      # move Obstacle to specified location
      self.positiveRectangle = self.rectangle
      self.positiveRectangle.centerx = centerX
      self.positiveRectangle.centery = centerY

      # display Obstacle in moved position to buffer visible area
      self.rectangle = self.positiveRectangle.move( -60, -60 )

   def move( self, xIncrement, yIncrement ):
      """Move Obstacle location up by specified increments"""
      
      self.positiveRectangle.centerx -= xIncrement
      self.positiveRectangle.centery -= yIncrement

      # change position for next pass
      if self.positiveRectangle.centery < 25:
         self.positiveRectangle[ 0 ] += \
            random.randrange( -640, 640 )

      # keep rectangle values from overflowing
      self.positiveRectangle[ 0 ] %= 760
      self.positiveRectangle[ 1 ] %= 600

      # display obstacle in moved position to buffer visible area
      self.rectangle = self.positiveRectangle.move( -60, -60 )

   def collisionBox( self ):
      """Return smaller bounding box for collision tests"""
      
      return self.rectangle.inflate( -20, -20 )

class Objective( Sprite ):
   """Moveable Objective Sprite"""

   def __init__( self, image, centerX = 0, centerY = 0 ):
      """Load Objective image and initialize rectangle"""

      Sprite.__init__( self, image )

      # move Objective to specified location
      self.rectangle.centerx = centerX
      self.rectangle.centery = centerY

   def move( self, xIncrement, yIncrement ):
      """Move Objective location up by specified increments"""
      
      self.rectangle.centerx -= xIncrement
      self.rectangle.centery -= yIncrement

# place a message on screen
def displayMessage( message, screen, background ):
   font = pygame.font.Font( None, 48 )
   text = font.render( message, 1, ( 250, 250, 250 ) )
   textPosition = text.get_rect()
   textPosition.centerx = background.get_rect().centerx
   textPosition.centery = background.get_rect().centery
   return screen.blit( text, textPosition )

# remove outdated time display and place updated time on screen
def updateClock( time, screen, background, oldPosition ):
   remove = screen.blit( background, oldPosition, oldPosition )
   font = pygame.font.Font( None, 48 )
   text = font.render( str( time ), 1, ( 250, 250, 250 ),
      ( 0, 0, 0 ) )
   textPosition = text.get_rect()
   post = screen.blit( text, textPosition )
   return remove, post

def main():

   # constants
   WAIT_TIME = 20            # time to wait between frames
   COURSE_DEPTH = 50 * 480   # 50 screens long
   NUMBER_ASTEROIDS = 20     # controls number of asteroids

   # variables
   distanceTraveled = 0      # vertical distance
   nextTime = 0              # time to generate next frame
   courseOver = 0            # the course has not been completed
   allAsteroids = []         # randomly generated obstacles
   dirtyRectangles = []      # screen positions that have changed
   energyPack = None         # current energy pack on screen
   timeLeft = 60             # time left to finish course
   newClock = ( 0, 0, 0, 0 ) # location of clock

   # find path to sounds
   collisionFile = os.path.join( "data", "collision.wav" )
   chimeFile = os.path.join( "data", "energy.wav" )
   startFile = os.path.join( "data", "toneup.wav" )
   applauseFile = os.path.join( "data", "applause.wav" )
   gameOverFile = os.path.join( "data", "tonedown.wav" )

   # find path to images
   shipFiles = []
   shipFiles.append( os.path.join( "data", "shipLeft.gif" ) )
   shipFiles.append( os.path.join( "data", "shipDown.gif" ) )
   shipFiles.append( os.path.join( "data", "shipRight.gif" ) )
   shipCrashFile = os.path.join( "data", "shipCrashed.gif" )
   asteroidFile = os.path.join( "data", "Asteroid.gif" )
   energyPackFile = os.path.join( "data", "Energy.gif" )

   # obtain user preference
   fullScreen = int( raw_input(
      "Fullscreen? ( 0 = no, 1 = yes ): " ) )

   # initialize pygame
   pygame.init()

   if fullScreen:
      screen = pygame.display.set_mode( ( 640, 480 ), FULLSCREEN )
   else:
      screen = pygame.display.set_mode( ( 640, 480 ) )
   
   pygame.display.set_caption( "Space Cruiser!" )
   pygame.mouse.set_visible( 0 )   # make mouse invisible

   # create background and fill with black
   background = pygame.Surface( screen.get_size() ).convert()

   # blit background onto screen and update entire display
   screen.blit( background, ( 0, 0 ) )
   pygame.display.update()

   collisionSound = pygame.mixer.Sound( collisionFile )
   chimeSound = pygame.mixer.Sound( chimeFile )
   startSound = pygame.mixer.Sound( startFile )
   applauseSound = pygame.mixer.Sound( applauseFile )
   gameOverSound = pygame.mixer.Sound( gameOverFile )

   # load images, convert pixel format and make white transparent
   loadedImages = []
   
   for file in shipFiles:
      surface = pygame.image.load( file ).convert()
      surface.set_colorkey( surface.get_at( ( 0, 0 ) ) )
      loadedImages.append( surface )

   # load crash image
   shipCrashImage = pygame.image.load( shipCrashFile ).convert()
   shipCrashImage.set_colorkey( shipCrashImage.get_at( ( 0, 0 ) ) )

   # initialize theShip
   centerX = screen.get_width() / 2
   theShip = Player( loadedImages, shipCrashImage, centerX, 25 )

   # load asteroid image
   asteroidImage = pygame.image.load( asteroidFile ).convert()
   asteroidImage.set_colorkey( asteroidImage.get_at( ( 0, 0 ) ) )
   
   # place asteroid in randomly generated spot
   for i in range( NUMBER_ASTEROIDS ):
      allAsteroids.append( Obstacle( asteroidImage,
         random.randrange( 0, 760 ), random.randrange( 0, 600 ) ) )

   # load energyPack image
   energyPackImage = pygame.image.load( energyPackFile ).convert()
   energyPackImage.set_colorkey( surface.get_at( ( 0, 0 ) ) )

   startSound.play()
   pygame.time.set_timer( USEREVENT, 1000 )

   while not courseOver:
   
      # wait if moving too fast for selected frame rate
      currentTime = pygame.time.get_ticks()
      
      if currentTime < nextTime:
         pygame.time.delay( nextTime - currentTime )
   
      nextTime = currentTime + WAIT_TIME
   
      # remove objects from screen
      dirtyRectangles.append( theShip.remove( screen,
         background ) )
      
      for asteroid in allAsteroids:    
         dirtyRectangles.append( asteroid.remove( screen,
            background ) )
   
      if energyPack is not None:
         dirtyRectangles.append( energyPack.remove( screen,
            background ) )

      # get next event from event queue
      event = pygame.event.poll()

      # if player quits program or presses escape key
      if event.type == QUIT or \
         ( event.type == KEYDOWN and event.key == K_ESCAPE ):
         sys.exit()

      # if up arrow key was pressed, slow ship
      elif event.type == KEYDOWN and event.key == K_UP:
         theShip.decreaseSpeed()

      # if down arrow key was pressed, speed up ship
      elif event.type == KEYDOWN and event.key == K_DOWN:
         theShip.increaseSpeed()      

      # if right arrow key was pressed, move ship right
      elif event.type == KEYDOWN and event.key == K_RIGHT:
         theShip.moveRight()

      # if left arrow key was pressed, move ship left 
      elif event.type == KEYDOWN and event.key == K_LEFT:
         theShip.moveLeft()

      # one second has passed
      elif event.type == USEREVENT:
         timeLeft -= 1
      
      # 1 in 100 odds of creating new energyPack
      if energyPack is None and not random.randrange( 100 ):
         energyPack = Objective( energyPackImage,
            random.randrange( 0, 640 ), 480 )

      # update obstacle and energyPack positions if ship moving
      if theShip.isMoving():
         xIncrement, yIncrement = theShip.distanceMoved()

         for asteroid in allAsteroids:
            asteroid.move( xIncrement, yIncrement )

         if energyPack is not None:
            energyPack.move( xIncrement, yIncrement )

            if energyPack.rectangle.bottom < 0:
               energyPack = None         

         distanceTraveled += yIncrement
   
      # check for collisions with smaller bounding boxes
      # for better playability
      asteroidBoxes = []

      for asteroid in allAsteroids:
         asteroidBoxes.append( asteroid.collisionBox() )

      # retrieve list of obstacles colliding with player
      collision = theShip.collisionBox().collidelist(
         asteroidBoxes )

      # move asteroid one screen down
      if collision != -1:
         collisionSound.play()
         allAsteroids[ collision ].move( 0, -540 )
         theShip.collision()
         timeLeft -= 5

      # determine whether player has gotten energyPack
      if energyPack is not None:

         if theShip.collisionBox().colliderect(
            energyPack.rectangle ):
            chimeSound.play()
            energyPack = None
            timeLeft += 5

      # place objects on screen
      dirtyRectangles.append( theShip.place( screen ) )

      for asteroid in allAsteroids:   
         dirtyRectangles.append( asteroid.place( screen ) )

      if energyPack is not None:
         dirtyRectangles.append( energyPack.place( screen ) )

      # update time
      oldClock, newClock = updateClock( timeLeft, screen,
         background, newClock )
      dirtyRectangles.append( oldClock )
      dirtyRectangles.append( newClock )

      # update changed areas of display
      pygame.display.update( dirtyRectangles )
      dirtyRectangles = []

      # check for course end
      if distanceTraveled > COURSE_DEPTH:
         courseOver = 1

      # check for game over
      elif timeLeft <= 0:
         break

   if courseOver:
      applauseSound.play()
      message = "Asteroid Field Crossed!"
   else:
      gameOverSound.play()
      message = "Game Over!"

   pygame.display.update( displayMessage( message, screen,
      background ) )

   # wait until player wants to close program
   while 1:
      event = pygame.event.poll()

      if event.type == QUIT or \
         ( event.type == KEYDOWN and event.key == K_ESCAPE ):
         break

if __name__ == "__main__":
   main()

########################################################################## 
# (C) Copyright 2002 by Deitel & Associates, Inc. and Prentice Hall.     #
# All Rights Reserved.                                                   #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
