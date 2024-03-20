import cv2
# Convert RGB to Grayscale

def convert_rgb2Gray(img_url):
    img = cv2.imread(img_url)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 