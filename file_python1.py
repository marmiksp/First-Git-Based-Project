
# In this Program, we will going to move
# file(.txt , .jpg etc) from source to Destination
# and not Folders


import os
import shutil
src = 'C:/Users/MSP/Desktop/A'
dest = 'C:/Users/MSP/Desktop/B'

filess = os.listdir(src)
print("A -> ",filess)

filesd = os.listdir(dest)
print("B -> ",filesd)
os.chdir(src)
#for fil in filess:        # this will create error 
#    shutil.copy(fil, dest) # of not copying folder
                           # to overcome that follow right next code

for fil in filess:

 	if os.path.isfile(fil):
 		shutil.copy(fil, dest)                          