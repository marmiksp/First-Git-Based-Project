# In this Program, we will going to move
# Folder from source to Destination

import os
import shutil
import distutils.dir_util

src = r'C:\Users\MSP\Desktop\A'
dest = r'C:\Users\MSP\Desktop\B'
i=1 # here u can also use random number for creating random name folders
k = "NEr"+str(i)
folder  =  os.path.join(src, "NewF")
dest_fol = os.path.join(dest,  k)
print(folder)
print(dest_fol)
#shutil.copytree(folder , dest_fol ) # here each and every time u need to create new folder so that there should not be overwright but it is still tedious job 
distutils.dir_util.copy_tree(folder , dest_fol ) # OVERWRIGHT || here u do not need to create new folder but it will overwright previous one.