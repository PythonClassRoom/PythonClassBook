<?xml version = "1.0"?>
<!-- Fig. 16.3: contact_list.xsl -->
<!-- Formats a contact list.     -->

<xsl:stylesheet version = "1.0" 
   xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

   <!-- match document root -->
   <xsl:template match = "/">

      <html xmlns = "http://www.w3.org/1999/xhtml">

         <head>
            <title>Contact List</title>
         </head>

         <body>
            <table border = "1">

               <thead>
                  <tr>
                     <th>First Name</th>
                     <th>Last Name</th>
                  </tr>
               </thead>

               <!-- process each contact element -->
               <xsl:for-each select = "contacts/contact">
                  <tr>
                     <td>
                        <xsl:value-of select = "FirstName" />
                     </td>
                     <td>
                        <xsl:value-of select = "LastName" />
                     </td>
                  </tr>
               </xsl:for-each>

            </table>

         </body>

      </html>

   </xsl:template>

<!-- 
 ************************************************************************** 
 * (C) Copyright 2002 by Deitel & Associates, Inc. and Prentice Hall.     *
 * All Rights Reserved.                                                   *
 *                                                                        *
 * DISCLAIMER: The authors and publisher of this book have used their     *
 * best efforts in preparing the book. These efforts include the          *
 * development, research, and testing of the theories and programs        *
 * to determine their effectiveness. The authors and publisher make       *
 * no warranty of any kind, expressed or implied, with regard to these    *
 * programs or to the documentation contained in these books. The authors *
 * and publisher shall not be liable in any event for incidental or       *
 * consequential damages in connection with, or arising out of, the       *
 * furnishing, performance, or use of these programs.                     *
 **************************************************************************
-->

</xsl:stylesheet>

