from PIL import Image
import hashlib
import time
from operator import itemgetter

#cracks
#http://SOMETHING/tools/captcha/image?image=4u0f635w4&v=2

name = 'EDUNXL'
im = Image.open('./crack/' + name + '.png')
im2 = Image.new("P",im.size,255)
im = im.convert("P")

temp = {}

his  = im.histogram()

values = {}

for i in range(256):
  values[i] = his[i]

for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
  print j,k
  
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

# New code is here. We just extract each image and save it to disk with
# what is hopefully a unique name

#im2.save('temp.png');
 
count = 0
for letter in letters:
  m = hashlib.md5()
  im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
  m.update("%s%s"%(time.time(),count))
  im3.save("./stuff/%s.gif"%(name[count]))
  count += 1
  print 'saved'
