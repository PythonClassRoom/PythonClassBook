<?xml version = "1.0"?>

<!-- Fig. 16.27: formatting.xsl   -->
<!-- Style sheet for forum files. -->

<xsl:stylesheet version = "1.0"
   xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

   <!-- match document root -->
   <xsl:template match = "/">
      <html xmlns = "http://www.w3.org/1999/xhtml">

      <!-- apply templates for all elements -->
      <xsl:apply-templates select = "*" />
      </html>
   </xsl:template>

   <!-- match forum elements -->
   <xsl:template match = "forum">
      <head>
         <title><xsl:value-of select = "name" /></title>
         <link rel = "stylesheet" type = "text/css"
            href = "../XML/site.css" />
      </head>

      <body>
         <table width = "100%" cellspacing = "0"
            cellpadding = "2">
            <tr>
               <td class = "forumTitle">
                  <xsl:value-of select = "name" />
               </td>
            </tr>
         </table>

         <!-- apply templates for message elements -->
         <br />
            <xsl:apply-templates select = "message" />
         <br />

         <div style = "text-align: center">
            <a>

               <!-- add href attribute to "a" element -->
               <xsl:attribute name = "href">../cgi-bin/addPost.py?file=<xsl:value-of select = "@file" />
               </xsl:attribute>
               Post a Message
            </a>
            <br /><br />
            <a href = "../cgi-bin/default.py">Return to Main Page</a>
         </div>

      </body>
   </xsl:template>

   <!-- match message elements -->
   <xsl:template match = "message">
      <table width = "100%" cellspacing = "0"
         cellpadding = "2">
         <tr>
            <td class = "msgTitle">
               <xsl:value-of select = "title" />
            </td>
         </tr>

         <tr>
            <td class = "msgInfo">
               by
               <xsl:value-of select = "user" />
               at
               <span class = "date">
                  <xsl:value-of select = "@timestamp" />
               </span>
            </td>
         </tr>

         <tr>
            <td class = "msgText">
               <xsl:value-of select = "text" />
            </td>
         </tr>

      </table>
   </xsl:template>

</xsl:stylesheet>

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
