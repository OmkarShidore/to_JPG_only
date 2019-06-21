"""

Created on Thu Jun 13 14:51:02 2019

@author: Omkar Shidore
@guthub: https://github.com/OmkarShidore


"""

import cv2 as cv
import os

#creating folder for output images
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
createFolder('./output_jpg/')

#using source image name to create the same name for output images
list1=os.listdir("source")
list2=[]
for name in list1:
    list2.append(''.join(name.split('.')[:-1]))
def img_to_jpg():
    i=0
    for name in list1:
        input_name=name
        img = cv.imread('source\\'+input_name,1)
        print(input_name)
        outpath_jpg='output_jpg\\'+list2[i]+'.jpg'
        cv.imwrite(outpath_jpg,img)
        cv.waitKey(0)
        cv.destroyAllWindows()
        i+=1

print("------------------------------------------------")
print("Starting Conversion.")
print("-------------------------------------------------")
img_to_jpg()
print("------------------------------------------------")
print("Image Conversion done, Check the Output folder.")
print("-------------------------------------------------")