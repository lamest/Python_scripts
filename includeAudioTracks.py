from pathlib import Path

currentPath=".\\"
outputPath="C:\watch\\"
    
videoFiles=list(Path(currentPath).glob("*.[mM][kK][vV]"))
audioFiles=list(Path(currentPath).rglob("*.[mM][kK][aA]"))

from os.path import splitext, basename

audioTracks=[]

class Video:
    def __init__(self, VideoFile):
        self.VideoFile = VideoFile
        self.AudioFiles = []

videos=[]
for i, videoFile in enumerate(videoFiles):
    videoFileName=splitext(basename(videoFile))[0]
    video=Video(videoFile)
    videos.append(video)
    for j, audioFile in enumerate(audioFiles):
        audioFileName=splitext(basename(audioFile))[0]
        if videoFileName==audioFileName:
            video.AudioFiles.append(audioFile)

from os import system

for video in videos:
    command=f"ffmpeg -i \"{video.VideoFile}\" "  
    for i, audio in enumerate(video.AudioFiles):
         command+= f"-i \"{audio}\" "
    command+="-map 0 "
    for i, audio in enumerate(video.AudioFiles):
        command+=f"-map {i+1}:a -metadata:s:a:{i+1} language=ru -metadata:s:a:{i+1} title=\"{audio.parts[-2]}\" " 
    command+=f"-c copy \"{outputPath}output_{basename(video.VideoFile)}\""
    system(command)