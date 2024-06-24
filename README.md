# pangGetImgs

## Intro
It's a tiny project made in Python designed to **efficiently** download multiple images from Google at once

## Preparations to do
1. Download [**`Python`**](https://www.python.org/downloads/ 'Download Python') in your system
   > Select the one that matches your operating system
2. Open your terminal
   > You can choose where to clone this repository
3. Clone this repository to your device with the command below
   ```
   git clone https://github.com/pangGou816/pangGetImgs.git
   ```
4. Go to the directory you've cloned
   ```
   cd pangGetImgs
   ```
5. Install all the dependencies with the command below
   ```
   python config.py
   ```

## How to use
 - Usage: `python pangGetImgs.py 'keyword' [output images amount]`
   > You **must** provide a keyword, and the number of output images is **optional**
   > The default number of output images is `7`

 - Decide what image you are interested in, then use the command below
   ```Python
   python pangGetImgs.py 'keyword'

   #For example, I really love the anime "Spy x Family". I can use:
   python pangGetImgs.py 'Spy x Family'
   ```
   > The **`'`** is a **must** if you have **space** in the keyword
 - After that, there will be an additional directory named after the keyword

 - To **modify** the number of output images, simply add an **`integer`** after the keyword
   ```Python
   python pangGetImgs.py 'Spy x Family' 77
   ```
 - After that, you can see an additional directory containing 77 images