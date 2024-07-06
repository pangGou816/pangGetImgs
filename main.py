import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests

import magic

import base64

def main() -> None:
   keyword = None
   requestAmount = 7
   if len( sys.argv ) == 2 or len( sys.argv ) == 3:
      if len( sys.argv ) == 2: keyword = sys.argv[1]
      else:
         keyword = sys.argv[1]
         try: requestAmount = int( sys.argv[2] )
         except ValueError:
            print( f'\nExpected an integer after "{keyword}"' )
            print( '\nUsing default value "7" as [output images amount]' )
         except Exception as error: print( error )
   else:
      print( '\nUsage: python pangGetImgs.py "keyword" [output images amount]\n' )
      sys.exit()

   chromeOption = Options()
   chromeOption.add_argument( 'blink-settings=imagesEnabled=false' )
   chromeOption.add_argument( '--disable-javascript' ) 
   chromeOption.add_argument( '--headless' )
   driver = webdriver.Chrome( chromeOption )
   driver.get( 'https://images.google.com/' )
   driver.set_window_size( 1920, 1080 )

   wait = WebDriverWait( driver, timeout=7 )
   wait.until( lambda d: driver.find_element( By.NAME, 'q' ).is_displayed() )

   print( f'\nSearching "{keyword}"...' )

   searchBar = driver.find_element( By.NAME, 'q' )
   searchBar.clear()
   searchBar.send_keys( keyword )
   searchBar.send_keys( Keys.RETURN )

   wait = WebDriverWait( driver, timeout=7 )
   wait.until( lambda d: driver.find_element( By.CLASS_NAME, 'mNsIhb' ).is_displayed() )

   for i in range( int( requestAmount / 13 ) ):
      driver.execute_script( 'window.scrollBy(0,1080)' )
      time.sleep( 5 )

   images = driver.find_elements( By.XPATH, './/img[@class="YQ4gaf"]' )

   try:
      dirPath = os.path.abspath( '../' + keyword )
      os.mkdir( dirPath )
   except:
      subscript = 0
      while True:
         try:
            dirPath = os.path.abspath( '../' + keyword + str( subscript ) )
            os.mkdir( dirPath )
            break
         except: subscript += 1

   print( f'\nDownloading into "{keyword}"...' )

   if requestAmount > len( images ): requestAmount = len( images )

   for i in range( requestAmount ):
      src = images[i].get_attribute( 'src' )
      imagePath = os.path.join( dirPath, f'{keyword}{i:>03}' )
      try:
         header, imageData = src.split( ',', 1 )
         fileSubscript = header.split( ';' )[0].split( '/' )[1]
         image = base64.b64decode( imageData )
         with open( imagePath + '.' + fileSubscript, 'wb' ) as imageFile:
            imageFile.write( image )
      except:
         responce = requests.get( src )
         with open( imagePath, 'wb' ) as imageFile:
            imageFile.write( responce.content )
         with open( imagePath, 'rb' ) as imageFile:
            fileSubscript = magic.from_buffer( imageFile.read(), mime=True ).split( '/' )[1]
         os.rename( imagePath, imagePath + '.' + fileSubscript )

   print( '\nFinish\n' )

   driver.quit()

if __name__ == '__main__':
   main()