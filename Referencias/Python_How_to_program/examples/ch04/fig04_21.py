# Fig. 4.21: fig04_21.py
# Keyword arguments example.

def generateWebsite( name, url = "www.deitel.com",
                      Flash = "no", CGI = "yes" ):
   print "Generating site requested by", name, "using url", url

   if Flash == "yes":
      print "Flash is enabled"

   if CGI == "yes":
      print "CGI scripts are enabled\n"   
   print

generateWebsite( "Deitel" )

generateWebsite( "Deitel", Flash = "yes",
                  url = "www.deitel.com/new" )

generateWebsite( CGI = "no", name = "Prentice Hall" )

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
