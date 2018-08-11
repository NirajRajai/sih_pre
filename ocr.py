from PIL import Image
import pytesseract
import argparse
import cv2
import os
import string
from bs4 import BeautifulSoup
import requests
import re
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                help="type of preprocessing to be done")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
f=open('text.txt','w')
f.write(text.encode('ascii', 'ignore'))
f.close()
#print(text.encode('ascii', 'ignore'))
ls=[]
for line in reversed(open("text.txt").readlines()):
    st=line.rstrip()
    if(st!=''):
        ls.append(st)
option1=ls[2]
option2=ls[1]
option3=ls[0]
ls.reverse()
question=' '.join(ls[0:len(ls)-3])

# show the output images
