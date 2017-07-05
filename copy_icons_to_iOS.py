from shutil import copyfile
import os

iOSPath="C:\\projects\\timeflip\\Sources\\TimeTracker\\TimeTracker.iOS\\Resources\\Media.xcassets\\"
imgPath='C:\\Users\\mn0055\\Desktop\\icons\\90\\'
imgs=os.listdir(imgPath)
for img in imgs:
   copyfile(imgPath+img, iOSPath+img[:-4]+"_icon.imageset\\"+img)