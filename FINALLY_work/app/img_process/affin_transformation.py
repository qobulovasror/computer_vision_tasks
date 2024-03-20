# Аффинные преобразования на основе уравнения
import random
import numpy as np
from PIL import Image, ImageDraw
import math
import matplotlib.pyplot as plt


def parallel_transfer(img_url, x, y):
    # parallel surish
    img = Image.open(img_url)
    width = img.size[0]
    height = img.size[1]

    img_new = Image.new(mode="L", size=(width * 2, height * 2))

    img_pix_new = img_new.load()
    pix = img.load()

    for i in range(width):
        for j in range(height):
            img_pix_new[i + x, j + y] = pix[i, j]

    return img_pix_new


def rotate_img(img_url, angile):
    image = Image.open(img_url)

    width = image.size[0]  
    height = image.size[1] 

    midx, midy = (width // 2, height // 2)

    alfa = math.pi * angile / 180
    alfa = math.radians(angile)
    imgnew = Image.new(mode="L", size=(width * 2, height * 2))
    pix = image.load() 

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
        # pix1[i,j]=255-pix[i, j];
        # draw.point((i, j), )
    # im = Image.fromarray(pix1, mode="L")
    # image.show()
    return imgnew







# image = Image.open("img2.jpg")
# width = image.size[0]
# height = image.size[1]

# imgnew = Image.new(mode="L", size=(width, height))
# imgnew2 = Image.new(mode="L", size=(width, height))
# imgnewdiff = Image.new(mode="L", size=(width, height))
# # imgnewdiff2  = Image.new( mode = "L", size = (width, height) )

# pix = image.load()

# imgnewpix = imgnew.load()
# imgnewpix2 = imgnew2.load()
# imgnewpixdiff = imgnewdiff.load()
# # imgnewpixdiff2=imgnewdiff2.load()

# for i in range(width):
#     for j in range(height):
#         imgnewpix[i, j] = (pix[i, j][0] + pix[i, j][1] + pix[i, j][2]) // 3
#         # o'rtacha qiymat bo'yicha
#         imgnewpix2[i, j] = int(
#             0.299 * pix[i, j][0] + 0.587 * pix[i, j][1] + 0.144 * pix[i, j][2]
#         )
#         # Average Method
#         imgnewpixdiff[i, j] = abs(imgnewpix2[i, j] - imgnewpix[i, j])  # farqi
#         # imgnewpixdiff2[i,j]=abs(imgnewpix[i,j]-imgnewpix2[i,j])

# fig = plt.figure(figsize=(15, 15))
# rows, columns = (3, 2)
# fig.add_subplot(rows, columns, 1)

# # showing image
# plt.imshow(imgnew, cmap="gray")
# plt.axis("off")
# plt.title("First")

# fig.add_subplot(rows, columns, 2)
# # showing image
# plt.imshow(image, cmap="gray")
# plt.axis("off")
# plt.title("Orginal")

# fig.add_subplot(rows, columns, 3)
# # showing image
# plt.imshow(imgnew2, cmap="gray")
# plt.axis("off")
# plt.title("Secund")

# fig.add_subplot(rows, columns, 4)
# # showing image
# plt.imshow(imgnewdiff, cmap="gray")
# plt.axis("off")
# plt.title("Diffence")

