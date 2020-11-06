from os import walk,system

mypath="D:\Downloads\Fullmetal Alchemist Brotherhood [BDRip] [1080p]\\"
files = []
for (_, _, filenames) in walk(mypath):
    files.extend(filenames)

audio = filter(lambda file: file.endswith('.mka'), files)
audio=list(audio)
video = filter(lambda file: file.endswith('.mkv'), files)
video=list(video)

for i, file in enumerate(video):
  system(f"ffmpeg -i \"{mypath}{file}\" -i \"{mypath}{audio[i]}\" -map 0 -map 1:a -c copy \"{mypath}output_{file}\"")