#!/usr/bin/env python3

from cv2 import cv2
import sys

CARACTERES = "@#$%?*+;:,.   "
PATH = "./images/1.jpg"

def main():
    image = cv2.imread(PATH, 0)
    #fichier = open("ascii.txt", "w")
    n = len(CARACTERES)

    width, height = image.shape[:2]
    if width > 100:
        new_height = height * 100 // width
        width = 100
        image = cv2.resize(image, (width, new_height))
        print(image.shape)
    for ligne in image:
        for pixel in ligne:
            print(CARACTERES[min(n - 1, pixel // (255 // n))], end=" ")
            #fichier.write(CARACTERES[min(n - 1, pixel // (255 // n))])
        #fichier.write('\n')
        print()
    #fichier.close()

if __name__ == "__main__":
    main()