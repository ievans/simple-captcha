from PIL import Image
import os
import math
import random
import operator
from operator import itemgetter
#from compare import compare_files
import ImageChops

def equal(im1, im2):
  if im1.size[0] != im2.size[0] or \
     im1.size[1] != im2.size[1]:
    return None
  else:
    off = 0
    for y in range(im2.size[0]): # slice across
      for x in range(im2.size[1]): # slice down
        if im2.getpixel((y, x)) != im1.getpixel((y, x)):
          off += 1
    return off

#cracks
#http://SOMETHING/tools/captcha/image?image=4u0f635w4&v=2

def train():
  trainingset = os.listdir('./trainingset')
  for name in trainingset:
    if name[0] == '.': continue
    images = split('./trainingset/' + name)
    if len(images) != 6:
      print 'bad image: ', name
      continue
    for letter, im in enumerate(images):
      im.save('./lib/' + name[letter] + '.' + str(random.randint(0, 1e10)) + '.png')
  print 'training complete, output in ./lib'
    
def decaptcha(filename):
  charImages = split(filename)
  r = ''
  for c in charImages:
    r += parseImage(c)
  return r

def parseImage(img):
  scores = []
  for potential in os.listdir('./lib'):
    if potential[0] == '.': continue
    pi = Image.open('./lib/' + potential)
    t = (equal(pi, img), potential[:potential.index('.')])
    if t[0] != None:
      scores.append(t)
  print scores
  return min(scores)[1]

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
#  im2.save('temp.png');

  count = 0
  imgs = []
  for letter in letters:
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    imgs.append(im3)
  return imgs
