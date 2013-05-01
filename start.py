"""
A simple programme for displaying text files
GitHub - https://github.com/anjanborah/Text_File_Viewer_Simple_Python
Author - Anjan Borah
Copyright ( c ) 2013 Anjan Borah
"""
import sys
import os
try:
  import Application
except( ImportError ) as exception:
  print >> sys.stdout, "Failed to import the Application module"
  sys.exit( 0 )

def main():
  try:
    if sys.platform.lower().startswith( "win" ):
      os.system( "cls" )
    if sys.platform.lower().startswith( "lin" ):
      os.system( "clear" )
    object = Application.Application()
  except( KeyboardInterrupt ) as exception:
    print >> sys.stdout, "\n+-------------------------------------------------------------+"
    print >> sys.stdout, "|                Keyboard interrupt received                  |"
    print >> sys.stdout, "|                 Programme is going to quit                  |"
    print >> sys.stdout, "+-------------------------------------------------------------+"
  except( Exception ) as exception:
    print >> sys.stdout, "Exception received - ", exception

if __name__ == "__main__":
  main()
