#!/usr/bin/python

import sys
from PIL import Image

def main():
    img = Image.new('RGB', (255, 255), "black")  # create a new black image
    pixels = img.load()  # create the pixel map

    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            pixels[i, j] = (i, j, 100)  # set the colour accordingly

    img.save("my_image.png", "png")
if __name__ == "__main__":
    sys.exit(main())