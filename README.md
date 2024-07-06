# pangGetImgs

## Intro
This is a tiny Python project designed to **efficiently** download multiple images from Google at once  
It can output a directory containing a number of images associated with the keyword provided

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
 - Usage: `python main.py 'keyword' [output images amount]`
   > `Keyword` **must** be provided  
   > `Output images amount` is **optional**. The default output images amount is **7**

 - **Search** by `keyword`
   ```Python
   python main.py 'keyword'

   # For example, I really love the anime "Spy x Family". I can use the command:
   python main.py 'Spy x Family'
   ```
   > The **`'`** is a **must** if you have **space** in the keyword

   After that, there will be an additional directory named after the keyword

 - **Modify** `output images amount`
   ```Python
   # Simply add an integer after the keyword
   python main.py 'Spy x Family' 77
   ```
   > **Must be in the same order as the command above**

   After that, you can see an additional directory containing 77 images