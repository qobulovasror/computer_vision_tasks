# Аффинные преобразования на основе уравнения
import os
import numpy as np
from PIL import Image, ImageDraw
import math
import matplotlib.pyplot as plt


def parallel_transfer(img_url, x, y):
    # parallel surish
    x = float(x)
    y = float(y)
    img = Image.open('app/static/uploaded_files/'+img_url) 

    bands = img.getbands()
    if bands == ('R','G','B') or bands== ('R','G','B','A'):
        img = img.convert('L')
        
    width = img.size[0]
    height = img.size[1]

    img_new = Image.new(mode="L", size=(width * 2, height * 2))

    img_pix_new = img_new.load()
    pix = img.load()

    for i in range(width):
        for j in range(height):
            img_pix_new[i + x, j + y] = pix[i, j]

    img_new.save(os.getcwd()+'/app/static/result_files/img1.png')
    return 'result_files/img1.png'


def rotate_img(img_url, angle):
    angle = float(angle)
    img = Image.open('app/static/uploaded_files/'+img_url) 

    bands = img.getbands()
    if bands == ('R','G','B') or bands== ('R','G','B','A'):
        img = img.convert('L')

    width = img.size[0]  
    height = img.size[1] 

    midx, midy = (width // 2, height // 2)

    alfa = math.pi * angle / 180
    alfa = math.radians(angle)
    imgnew = Image.new(mode="L", size=(width * 2, height * 2))
    pix = img.load() 

    imgnewpix = imgnew.load()

    cx, cy = (2 * width // 2, 2 * height // 2)

    for i in range(2 * width):
        for j in range(2 * height):
            imgnewpix[i, j] = 150

    for i in range(width):
        for j in range(height):
            x = (i - midx) * math.cos(alfa) + (j - midy) * math.sin(alfa)
            y = -(i - midx) * math.sin(alfa) + (j - midy) * math.cos(alfa)

            x = round(x) + cx
            y = round(y) + cy

            imgnewpix[x, y] = pix[i, j]
            
    imgnew.save(os.getcwd()+'/app/static/result_files/img1.png')
    return 'result_files/img1.png'




def convert_rgb_to_gray2():
    image = Image.open("img2.jpg")
    width = image.size[0]
    height = image.size[1]

    imgnew = Image.new(mode="L", size=(width, height))
    imgnew2 = Image.new(mode="L", size=(width, height))
    imgnewdiff = Image.new(mode="L", size=(width, height))
    # imgnewdiff2  = Image.new( mode = "L", size = (width, height) )

    pix = image.load()

    imgnewpix = imgnew.load()
    imgnewpix2 = imgnew2.load()
    imgnewpixdiff = imgnewdiff.load()
    # imgnewpixdiff2=imgnewdiff2.load()

    for i in range(width):
        for j in range(height):
            imgnewpix[i, j] = (pix[i, j][0] + pix[i, j][1] + pix[i, j][2]) // 3
            # o'rtacha qiymat bo'yicha
            imgnewpix2[i, j] = int(
                0.299 * pix[i, j][0] + 0.587 * pix[i, j][1] + 0.144 * pix[i, j][2]
            )
            # Average Method
            imgnewpixdiff[i, j] = abs(imgnewpix2[i, j] - imgnewpix[i, j])  # farqi
            # imgnewpixdiff2[i,j]=abs(imgnewpix[i,j]-imgnewpix2[i,j])

    fig = plt.figure(figsize=(15, 15))
    rows, columns = (3, 2)
    fig.add_subplot(rows, columns, 1)

    # showing image
    plt.imshow(imgnew, cmap="gray")
    plt.axis("off")
    plt.title("First")

    fig.add_subplot(rows, columns, 2)
    # showing image
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.title("Orginal")

    fig.add_subplot(rows, columns, 3)
    # showing image
    plt.imshow(imgnew2, cmap="gray")
    plt.axis("off")
    plt.title("Secund")

    fig.add_subplot(rows, columns, 4)
    # showing image
    plt.imshow(imgnewdiff, cmap="gray")
    plt.axis("off")
    plt.title("Diffence")

