# Fig. 24.5: fig24_05.py
# Playing an MPEG movie. 

import os
import sys
import pygame, pygame.movie
import pygame.mouse, pygame.image
from pygame.locals import *

def createGUI( file ):

   # load movie
   movie = pygame.movie.Movie( file )
   width, height = movie.get_size()

   # initialize display window
   screen = pygame.display.set_mode( ( width, height + 100 ) )
   pygame.display.set_caption( "Movie Player" )
   pygame.mouse.set_visible( 1 )

   # play button
   playImageFile = os.path.join( "data", "play.png" )
   playImage = pygame.image.load( playImageFile ).convert()
   playImageSize = playImage.get_rect()
   playImageSize.center = width / 2, height + 50

   # copy play button to screen
   screen.blit( playImage, playImageSize )
   pygame.display.flip()

   # set output surface for movie's video
   movie.set_display( screen )

   return movie, playImageSize

def main():

   # check command line arguments
   if len( sys.argv ) != 2:
      sys.exit( "Incorrect number of arguments." )
   else:
      file = sys.argv[ 1 ]
      
   # initialize pygame
   pygame.init()

   # initialize GUI
   movie, playImageSize = createGUI( file )

   # wait until player wants to close program
   while 1:
      event = pygame.event.wait()

      # close window
      if event.type == QUIT or \
         ( event.type == KEYDOWN and event.key == K_ESCAPE ):
         break

      # click play button and play movie
      pressed = pygame.mouse.get_pressed()[ 0 ]
      position = pygame.mouse.get_pos()

      # button pressed
      if pressed:

         if playImageSize.collidepoint( position ):
            movie.play()

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
