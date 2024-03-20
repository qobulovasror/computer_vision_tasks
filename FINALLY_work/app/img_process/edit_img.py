import random
import numpy as np
from PIL import Image, ImageDraw 
import math
import os
import cv2


def inkassator_img(img_url) -> Image.Image:
    """Generates an image of the Inkasso-Torpedo (TM) using Pillow library."""
    try:
        img = Image.open(img_url)

        width = img.size[0]
        height = img.size[1]

        img_new = Image.new(mode="L", size=(width, height))

        img_pix_new = img_new.load()
        
        pix = img.load()

        for i in range(width):
            for j in range(height):
                img_pix_new[i,j]=255-pix[i, j]
        new_url = 'inkassator_{}.png'.format(random.randint(1e6, 9e6))
        # Save the modified image to a file
        img_new.save(new_url)
        return img_new, new_url
    
    except Exception as e:
        print("Error processing image: ", str(e))
        raise ValueError('Invalid image URL')

# metod 1
def change_contrast1(img_url, c)->Image.Image:
    """Increases or decreases contrast of an image by modifying pixel values."""
    c = float(c)
    image = Image.open('app/static/uploaded_files/'+img_url) 

    bands = image.getbands()
    if bands == ('R','G','B') or bands== ('R','G','B','A'):
        image = image.convert('L')
        # raise Exception("It is RGB image, you can sent only Grayscale image")
    width = image.size[0]  
    height = image.size[1] 
    
    img_new = Image.new(mode="L", size=(width, height))

    pix = image.load()
    pix1 = img_new.load()
    for i in range(width):
        for j in range(height):
            T=c*int(math.log10(1+(pix[i, j])))
            if T == '':
                T = 0
            if int(T)<0:
                pix1[i,j]=int(0)
                
            elif int(T)>255:
                pix1[i,j]=int(255)
                
            else:
                pix1[i,j]=int(T)
            
            
    img_new.save(os.getcwd()+'/app/static/result_files/img1.png')
    return 'result_files/img1.png'

#metod 2
def change_contrast2(img_url, c=1, gamma=2)->Image.Image:
    """Increases or decreases contrast of an image by modifying pixel values."""
    c = float(c)
    gamma = float(gamma)

    image = Image.open('app/static/uploaded_files/'+img_url).convert('L')

    bands = image.getbands()
    if bands == ('R','G','B') or bands== ('R','G','B','A'):
        image = image.convert('L')
        # raise Exception("It is RGB image, you can sent only Grayscale image")
    width = image.size[0]  
    height = image.size[1]  
    
    img_new = Image.new(mode="L", size=(width, height))

    pix = image.load()
    pix1 = img_new.load()
    for i in range(width):
        for j in range(height):
            T=c*int(math.pow(pix[i, j],gamma)/math.pow(255,gamma-1))
            
            if int(T)<0:
                pix1[i,j]=int(0)
            elif int(T)>255:
                pix1[i,j]=int(255)
            else:
                pix1[i,j]=int(T)

    img_new.save(os.getcwd()+'/app/static/result_files/img1.png')
    return 'result_files/img1.png'



#img convert RGB to Grayscale
def convertImgRgb2Gray(img_url)->Image.Image:
    """Increases or decreases contrast of an image by modifying pixel values."""
    image = Image.open('app/static/uploaded_files/'+img_url).convert('L')
    image.save(os.getcwd()+'/app/static/result_files/img1.png')
    return 'result_files/img1.png'


#img convert Grayscale to RGB  
def convertImgGray2Rgb(img_url)->Image.Image:
    """Converts a grayscale image into RGB image"""
    # Load grayscale  image as B&W (Black and White)
    img_gray = cv2.imread('app/static/uploaded_files/'+img_url, cv2.IMREAD_GRAYSCALE)

    # Convert grayscale to RGB
    img_rgb = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

    # Save RGB image
    cv2.imwrite(os.getcwd()+'/app/static/result_files/img1.png', img_rgb)
    return 'result_files/img1.png'