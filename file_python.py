
# In this Program, we will listing the folder 
# and their subfolder and files
# Also i have done some code for print function

import os
import shutil

Dr = 'C:/Python 3.7 codes/Face Detection with Details'  
ma = 'C:/Python 3.7 codes/T2.txt'
for r, s, f in os.walk(Dr):
	print('Root => ',r)
	print('Subfolder => ',s)
	print('Files => ',f)
	# for file in f:
 #        path = os.path.join(r, file)
 #        print(path)

i=9
j=i
i=i+1
print("\n")
print("i = %d , j = %d" %(i,j))
print("i = ",i,"j = ",j)

#shutil.move(Dr,ma)