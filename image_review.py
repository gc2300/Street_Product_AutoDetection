import os
import glob
import numpy as np
import scipy.ndimage as nd
from os import listdir
from os.path import isfile, join
import scipy as sp
from scipy import linalg, dot
from skimage.measure import compare_ssim as ssim

THRESH = 0.98 #declaring this threshold above
path = os.getcwd()+'/input_img'
img_path = os.getcwd()+'/tmp'
myfiles = [f[:-4] for f in listdir(path) if isfile(join(path, f))]


DEBUG = True
for item in myfiles:
    images = []
    image_names = []
    for file in os.listdir("tmp"):
        if file.startswith(item):
            images.append(nd.imread(join(img_path,file)))
            image_names.append(file)


#score_matrix = []    
    images = np.array(images)
    image_names = np.array(image_names)
#if DEBUG: print (images)
#print(images[0])
#retain = np.zeros_like(images, bool) * np.nan
    retain = np.zeros(len(images), bool) * np.nan

    retain[0] = True
    for i, im in enumerate(images): #changed for clarity and efficiency
        if DEBUG: print (i)
        
        if not retain[i]:
            continue
        
        for j in range(i+1, len(images)):
            if not retain[j]:
                continue
            
            a = im
            b = images[j]
            score = ssim(a, b, multichannel=True)
            retain[j] = score < THRESH
        
    retain = retain > 0
    #print(images[retain])
    print(image_names[retain])
    print(len(images[retain]))
    with open("saved_images.txt", "a") as f:
        for image in image_names[retain]:
            f.write(image)
            
