# Fig. 22.4: fig22_04.py
# Driver to test class List.

from ListModule import List

# instructions for user
instructions = """Enter one of the following:
   1 to insert at beginning of list
   2 to insert at end of list
   3 to delete from beginning of list
   4 to delete from end of list
   5 to end list processing\n"""

listObject = List()  # create empty List
print instructions  # print instructions

# obtain user choice until user chooses to quit (choice 5)
while 1:

   choice = raw_input("\n? ") 

   # insert at front
   if choice == "1":
      listObject.insertAtFront( raw_input( "Enter value: " ) )
      print "The list is: ", listObject

   # insert at end
   elif choice == "2":
      listObject.insertAtBack( raw_input( "Enter value: " ) )
      print "The list is: ", listObject

   # delete from front
   elif choice == "3":

      try:
         value = listObject.removeFromFront()
      except IndexError, message:
         print "Failed to remove:", message
      else:
         print value, "removed from list"
         print "The list is: ", listObject

   # delete from end
   elif choice == "4":

      try:
         value = listObject.removeFromBack()
      except IndexError, message:
         print "Failed to remove:", message
      else:
          print value, "removed from list"
          print "The list is: ", listObject

   # exit
   elif choice == "5":
      break  # terminate while loop

   # invalid choice   
   else:
      print "Invalid choice:", choice
      print instructions

print "End list test\n"

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
