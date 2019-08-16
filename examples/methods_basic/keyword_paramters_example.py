
# Keyword arguments example.

def generateWebsite( name, url = "www.deitel.com",
                      Flash = "no", CGI = "yes" ):
   print("Generating site requested by", name, "using url", url)

   if Flash == "yes":
      print("Flash is enabled")

   if CGI == "yes":
      print("CGI scripts are enabled\n")
   print

generateWebsite( "Deitel" )

generateWebsite( "Deitel", Flash = "yes",
                  url = "www.deitel.com/new" )

generateWebsite( CGI = "no", name = "Prentice Hall" )
