import sys
import os

def main() -> None:
   os.system( 'pip uninstall selenium requests python-magic-bin' )
   os.system( 'pip install selenium==4.22.0' )
   os.system( 'pip install requests==2.32.3' )
   os.system( 'pip install python-magic-bin==0.4.14' )
   sys.exit()

if __name__ == '__main__':
   main()