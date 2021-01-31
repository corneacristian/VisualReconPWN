import cv2
import os
import numpy as np
from PIL import Image
import random

os.mkdir("results/")
image_path = input("Enter full path of the image : ")
image = Image.open(image_path)
image = image.convert("RGBA")
pixdata = image.load()
width, height = image.size
color = (0, 0, 0, 255)

os.mkdir("results/One_Pixel_Derivation/")
print("[+] Creating One Pixel Derivation Images Set")
for x in range(width):
    for y in range(height):
        pixdata_old = pixdata[x, y]
        pixdata[x, y] = color
        image.save("results/One_Pixel_Derivation/opd"+str(x)+str(y)+".png")
        pixdata[x, y] = pixdata_old


os.mkdir("results/Random_Pixel_Derivation/")
print("[+] Creating Random Pixel Derivation Images Set")
for i in range(50):
    randx = random.randint(3, width-3)
    randy = random.randint(3, height-3)
    pixdata_old1 = pixdata[randx, randy]
    pixdata_old2 = pixdata[randx+1, randy+1]
    pixdata_old3 = pixdata[randx+2, randy+1]
    pixdata[randx, randy] = color
    pixdata[randx+1, randy+1] = color
    pixdata[randx+2, randy+1] = color
    image.save("results/Random_Pixel_Derivation/rpd"+str(i)+".png")
    pixdata[randx, randy] = pixdata_old1
    pixdata[randx+1, randy+1] = pixdata_old2
    pixdata[randx+2, randy+1] = pixdata_old3


os.mkdir("results/Increased_Pixel_Derivation/")
print("[+] Creating Increased Pixel Derivation Images Set")
for x in range(width):
    for y in range(height):
        pixdata_old = pixdata[x, y]
        pixdata[x, y] = color
        image.save("results/Increased_Pixel_Derivation/ipd" +
                   str(x)+str(y)+".png")


