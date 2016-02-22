#!/usr/bin/env python
# requires pillow scipy and NumPy. Python 3.5
import scipy
from scipy import ndimage

# This block is JPG selector from current folder block
import os

ListOfPictures = []
for file in os.listdir():
    if file.endswith(".jpg"):
        # print(file)
        ListOfPictures.append(file)
print('Following pictures will be analysed:', ListOfPictures)
print('Number of pictures:', len(ListOfPictures))

# this block is doing graphical things
# print (ListOfPictures)

Count = []
try:
    for i in ListOfPictures:  # read image into numpy array
        Object = scipy.misc.imread(i)  # gray-scale image

        Objectf = ndimage.gaussian_filter(Object,2)  # default 16 # smooth the image (to remove small objects); set the threshold
        T = 50  # def 25

        # set threshold by hand to avoid installing `mahotas` or )
        # `scipy.stsci.image` dependencies that have threshold() functions
        # find connected components
        labeled, nr_objects = ndimage.label(Objectf > T)  # `Object[:,:,0]>T` for red-dot case
        print(i)
        print(nr_objects)
        Count.append(nr_objects)
        # print ("Number of objects is %d ") % nr_objects
        # show labeled image
        ####scipy.misc.imsave('labeled_Object.png', labeled)
        ####scipy.misc.imshow(labeled) # black&white image
        import matplotlib.pyplot as plt

        plt.imsave(i, labeled)
        plt.imshow(labeled)
        # plt.show()
except:
    pass

#results output
print(ListOfPictures)
print(Count)
ListOfLists=[]
ListOfLists.append(ListOfPictures)
ListOfLists.append(Count)
print (ListOfLists)
print('Graphical part Done')

#Transposition block
import numpy as np
ListOfListArray=np.array (ListOfLists)
print(ListOfListArray)
TransposedListOfListArray=np.transpose(ListOfListArray)
print(TransposedListOfListArray)

#Export block
import csv
csvfile = ('results.csv') #file name
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(TransposedListOfListArray)