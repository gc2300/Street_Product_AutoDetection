import numpy as np
import scipy.ndimage as nd
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import scipy as sp
#read in image

np.random.seed(200)
path = os.getcwd()+'/input_img'

inputs = [f for f in listdir(path) if isfile(join(path, f))]
for i in range(len(inputs)):
    fname = inputs[i]
    csb = nd.imread(join(path,fname))
    
    for j in range(5):
        s_vs_p = 0.5
        amount = 0.004
        out = csb
        # Generate Salt '1' noise
        num_salt = np.ceil(amount * csb.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in csb.shape]
        out[coords] = 255
        # Generate Pepper '0' noise
        num_pepper = np.ceil(amount* csb.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in csb.shape]
        out[coords] = 0
        sp.misc.imsave('./tmp/'+ fname[:-4] + '-sp-' +str(j)+'.jpg', out)
    
    
    
    
#     for j in range(5):
#         #adding noise in a gaussian distribution with standard deviation 0.01
#         img_ = csb.astype(float) * np.abs(np.random.randn(*csb.shape) * 0.001) 
#         #renormalize
#         img_ /= img_.max(0).max(0).shape
#         sp.misc.imsave('./sp_tmp_v2/'+ fname + '-sp-' +str(j)+'.png', img_)
