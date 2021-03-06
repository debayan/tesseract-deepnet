#!/usr/bin/python

from PIL import Image
import os,sys

charDict = {}

count = 0
charCount = -1
for root, dirs, files in os.walk(sys.argv[1]):
    path = root.split('/')
    for file in files:
        if 'box' in file:
            img = Image.open(root+file[:-4]+'.g4.tif')
            (width, height) = img.size
            f = open(root+file)
            for line in f.readlines():
                count += 1
                linearray = line.split(' ')
                charwidth = int(linearray[3]) - int(linearray[1])
                charheight = int(linearray[4]) - int(linearray[2])
                (tl1,tl2,br1,br2) = (int(linearray[1]), height - (int(linearray[2]) + charheight) , int(linearray[3]), height - (int(linearray[4]) - charheight))
                if not charDict.has_key(linearray[0]):
                    charCount += 1
                    charDict[linearray[0]] = charCount
                character = img.crop((tl1,tl2,br1,br2))
                character.save(sys.argv[2]+'/'+str(count)+'.jpg')
                print sys.argv[2]+'/'+str(count)+'.jpg',
                print charDict[linearray[0]]

