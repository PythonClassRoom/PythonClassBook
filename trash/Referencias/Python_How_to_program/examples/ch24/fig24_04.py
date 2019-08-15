# Fig. 24.4: fig24_04.py
# Simple CD player using Tkinter and pygame.

import sys
import string
import pygame, pygame.cdrom
from Tkinter import *
from tkMessageBox import *
import Pmw

class CDPlayer( Frame ):
   """A GUI CDPlayer class using Tkinter and pygame"""

   def __init__( self ):
      """Initialize pygame.cdrom and get CDROM if one exists"""
      
      pygame.cdrom.init()

      if pygame.cdrom.get_count() > 0:
         self.CD = pygame.cdrom.CD( 0 )
      else:
         sys.exit( "There are no available CDROM drives." )
         
      self.createGUI()
      self.updateTime()

   def destroy( self ):
      """Stop CD, uninitialize pygame.cdrom and destroy GUI"""

      if self.CD.get_init():
         self.CD.stop()

      pygame.cdrom.quit()
      Frame.destroy( self )

   def createGUI( self ):
      """Create CDPlayer widgets"""
      
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "CD Player" )

      # display current track playing
      self.trackLabel = IntVar()
      self.trackLabel.set( 1 )
      self.trackDisplay = Label( self, font = "Courier 14", 
         textvariable = self.trackLabel, bg = "black", 
         fg = "green" )
      self.trackDisplay.grid( sticky = W+E+N+S )

      # display current time of track playing
      self.timeLabel = StringVar()
      self.timeLabel.set( "00:00/00:00" )
      self.timeDisplay = Label( self, font = "Courier 14",
         textvariable = self.timeLabel, bg = "black",
         fg = "green" )
      self.timeDisplay.grid( row = 0, column = 1, columnspan = 3,
         sticky = W+E+N+S )

      # play/pause CD
      self.playLabel = StringVar()
      self.playLabel.set( "Play" )
      self.play = Button( self, textvariable = self.playLabel,
         command = self.playCD, width = 10 )
      self.play.grid( row = 1, column = 0, columnspan = 2,
         sticky = W+E+N+S )

      # stop CD
      self.stop = Button( self, text = "Stop", width = 10,
         command = self.stopCD )
      self.stop.grid( row = 1, column = 2, columnspan = 2,
         sticky = W+E+N+S )

      # skip to previous track
      self.previous = Button( self, text = "|<<", width = 5,
         command = self.previousTrack )
      self.previous.grid( row = 2, column = 0, sticky = W+E+N+S )

      # skip to next track
      self.next = Button( self, text = ">>|", width = 5,
         command = self.nextTrack )
      self.next.grid( row = 2, column = 1, sticky = W+E+N+S )

      # eject CD
      self.eject = Button( self, text = "Eject", width = 10,
         command = self.ejectCD )
      self.eject.grid( row = 2, column = 2, columnspan = 2,
         sticky = W+E+N+S )

   def playCD( self ):
      """Play/Pause CD if disc is loaded"""

      # if disc has been ejected, reinitialize drive
      if not self.CD.get_init():
         self.CD.init()
         self.currentTrack = 1

         # if no disc in drive, uninitialize and return
         if self.CD.get_empty():
            self.CD.quit()
            return

         # if disc is loaded, obtain disc information
         else:
            self.totalTracks = self.CD.get_numtracks()
            
      # if CD is not playing, play CD
      if not self.CD.get_busy() and not self.CD.get_paused():
         self.CD.play( self.currentTrack - 1 )
         self.playLabel.set( "| |" )

      # if CD is playing, pause disc         
      elif not self.CD.get_paused():
         self.CD.pause()
         self.playLabel.set( "Play" )

      # if CD is paused, resume play
      else:
         self.CD.resume()
         self.playLabel.set( "| |" )

   def stopCD( self ):
      """Stop CD if disc is loaded"""

      if self.CD.get_init():
         self.CD.stop()
         self.playLabel.set( "Play" )

   def playTrack( self, track ):
      """Play track if disc is loaded"""

      if self.CD.get_init():      
         self.currentTrack = track
         self.trackLabel.set( self.currentTrack )

         # start beginning of track
         if self.CD.get_busy():
            self.CD.play( self.currentTrack - 1 )
         elif self.CD.get_paused():
            self.CD.play( self.currentTrack - 1 )
            self.playCD()   # re-pause CD

   def nextTrack( self ):
      """Play next track on CD if disc is loaded"""

      if self.CD.get_init() and \
         self.currentTrack < self.totalTracks:
         self.playTrack( self.currentTrack + 1 )

   def previousTrack( self ):
      """Play previous track on CD if disc is loaded"""

      if self.CD.get_init() and self.currentTrack > 1:
         self.playTrack( self.currentTrack - 1 )

   def ejectCD( self ):
      """Eject CD from drive"""
   
      response = askyesno( "Eject pushed", "Eject CD?" )

      if response:
         self.CD.init()   # CD must be initialized to eject
         self.CD.eject()
         self.CD.quit()
         self.trackLabel.set( 1 )
         self.timeLabel.set( "00:00/00:00" )
         self.playLabel.set( "Play" )

   def updateTime( self ):
      """Update time display if disc is loaded"""

      if self.CD.get_init():
         seconds = int( self.CD.get_current()[ 1 ] )
         endSeconds = int( self.CD.get_track_length(
            self.currentTrack - 1 ) )

         # if reached end of current track, play next track
         if seconds >= ( endSeconds - 1 ):
            self.nextTrack()
         else:      
            minutes = seconds / 60
            endMinutes = endSeconds / 60
            seconds = seconds - ( minutes * 60 )
            endSeconds = endSeconds - ( endMinutes * 60 )

            # display time in format mm:ss/mm:ss   
            trackTime = string.zfill( str( minutes ), 2 ) + \
               ":" + string.zfill( str( seconds ), 2 )
            endTime = string.zfill( str( endMinutes ), 2 ) +  \
               ":" + string.zfill( str( endSeconds ), 2 )

            if self.CD.get_paused():
      
               # alternate pause symbol and time in display
               if not self.timeLabel.get() == "     ||    ":
                  self.timeLabel.set( "     ||    " )
               else:
                  self.timeLabel.set( trackTime + "/" + endTime )

            else:
               self.timeLabel.set( trackTime + "/" + endTime )

      # call updateTime method again after 1000ms ( 1 second )
      self.after( 1000, self.updateTime )

def main():
   CDPlayer().mainloop()

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
