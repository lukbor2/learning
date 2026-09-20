import shutil
import os

src_file = 'rsatcustominstaller.log'
src_folder = 'C:\\'
dst = 'C:\\temp'
src = src_folder + src_file

print("src: %s" %src)

res = shutil.copy(src,dst, follow_symlinks=True)

print ("res: %s" %res)
