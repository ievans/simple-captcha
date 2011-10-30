from PIL import Image
import os
import time
from operator import itemgetter
from compare import 
#cracks
#http://SOMETHING/tools/captcha/image?image=4u0f635w4&v=2

def train():
  trainingset = os.listdir('./trainingset')
  for name in trainingset:
    images = split(i)
    for letter, im in images:
       im.save('./lib/' + name[letter] + '.png')

def decaptcha(filename):
  charImages = split(filename)
  r = ''
  for c in charImages:
    r += parseImage(c)
  return r

def parseImage(img):
  for potential in os.listdir('./lib'):
    if compare_images(potential, img) == 0:
      return potential[:potential.index('.')]
  raise Exception('could not decaptcha the image!')

def split(filename):
  im = Image.open(filename)
  im2 = Image.new("P",im.size,255)
  im = im.convert("P")

  temp = {}
  ## his  = im.histogram()
  ## values = {}
  ## for i in range(256):
  ##   values[i] = his[i]
  ## for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
  ##   print j,k

  for x in range(im.size[1]):
    for y in range(im.size[0]):
      pix = im.getpixel((y,x))
      temp[pix] = pix
      if pix == 217:
        im2.putpixel((y,x),0)

  inletter = False
  foundletter=False
  start = 0
  end = 0

  letters = []

  for y in range(im2.size[0]): # slice across
      for x in range(im2.size[1]): # slice down
          pix = im2.getpixel((y,x))
          if pix != 255:
              inletter = True
      if foundletter == False and inletter == True:
          foundletter = True
          start = y
      if foundletter == True and inletter == False:
          foundletter = False
          end = y
          letters.append((start,end))
      inletter=False
  #im2.save('temp.png');

  count = 0
  imgs = []
  for letter in letters:
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    imgs.append(img3]
  return imgs

def find_image(file1, file2):
  img1 = to_grayscale(imread(file1).astype(float))
  img2 = to_grayscale(imread(file2).astype(float))
  # compare
  n_m, n_0 = compare_images(img1, img2)
  return n_0
  print "Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size
  print "Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size
