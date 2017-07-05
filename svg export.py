import os, subprocess, sys

incscapePath='C:\\Users\\mn0055\\Desktop\\inkscape\\inkscape.exe'
sourceFolder="C:\\Users\\mn0055\\Desktop\\icons\\svg_icons"
destFolder="C:\\Users\\mn0055\\Desktop\\icons"
svgs=os.listdir('C:\\Users\\mn0055\\Desktop\\icons\\svg_icons')

for svg in svgs:
     sys.stdout.write("Processing: %s%   \n" % (svg) )
     args=[incscapePath,"-z",sourceFolder+"\\"+svg,"-e",destFolder+"\\30\\"+svg[:-3]+"png","-w","30"]
     subprocess.call(args)
     args=[incscapePath,"-z",sourceFolder+"\\"+svg,"-e",destFolder+"\\60\\"+svg[:-3]+"png","-w","60"]
     subprocess.call(args)
     args=[incscapePath,"-z",sourceFolder+"\\"+svg,"-e",destFolder+"\\90\\"+svg[:-3]+"png","-w","90"]
     subprocess.call(args)
     args=[incscapePath,"-z",sourceFolder+"\\"+svg,"-e",destFolder+"\\110\\"+svg[:-3]+"png","-w","110"]
     subprocess.call(args)
