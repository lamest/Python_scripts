import subprocess

incscapePath=r"C:\Users\mn0055\Desktop\inkscape\inkscape.exe"
destFolder=r"C:\Users\mn0055\Desktop\icons\timeflip_logo"
svgName="logo_time_flip_color"
svg="C:\\Users\\mn0055\\Desktop\\icons\\timeflip_logo\\"+svgName+".svg"

args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"29"+".png","-w","29"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"40"+".png","-w","40"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"58"+".png","-w","58"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"76"+".png","-w","76"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"80"+".png","-w","80"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"87"+".png","-w","87"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"120"+".png","-w","120"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"152"+".png","-w","152"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"167"+".png","-w","167"]
subprocess.call(args)
args=[incscapePath,"-z",svg,"-e",destFolder+"\\"+svgName+"180"+".png","-w","180"]
subprocess.call(args)
