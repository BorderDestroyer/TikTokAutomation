import moviepy.editor
import os
import random

times = 0
for file in os.listdir("./Recordings"):
    times += 1
    recordingClip = moviepy.editor.AudioFileClip(f"./Recordings/{file}")
    mainClip = moviepy.editor.VideoFileClip("./BRoll.mp4")

    recordingLength = int(recordingClip.duration)
    mainClipLength = int(mainClip.duration)
    startPoint = random.randint(5, mainClipLength - recordingLength - 2)
    mainClipSub = mainClip.subclip(startPoint, startPoint + recordingLength + 1)
    
    finalClip = mainClipSub.set_audio(recordingClip).crop(x1=500, y1=50, x2=1220, y2=1030).resize(newsize=(720, 1280))
    finalClip.write_videofile(f"./FinalVids/Vid#{times}.mp4", fps=30)
