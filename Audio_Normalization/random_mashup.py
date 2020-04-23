from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment
import sys
import os
from os import listdir
from os.path import isfile, join
import numpy as np
from random import randint

class Video:
    def __init__(self, aud, start, t):
        self.video_clip = aud
        self.duration = start
        self.t = t

class VideoClip:
    def __init__(self, aud, start, end):
        self.video_clip_name = aud
        self.video_start = start
        self.video_end = end

folder_name = sys.argv[1]
#file_names = os.listdir(folder_name)
file_names = [f for f in listdir(folder_name) if isfile(join(folder_name, f))]

print(file_names)
video_list = []
video_clip_list = []

for i in range(len(file_names)):
    file1 = folder_name + file_names[i]
    audio_clip = AudioSegment.from_file(file1, "mp4")
    temp_video = Video(file1, audio_clip.duration_seconds, 0)
    video_list.append(temp_video)

num_videos = len(file_names)

count_videos = num_videos

while count_videos > 0:
    choosen_vid = randint(0,count_videos-1)
    gap=round(np.random.normal(2.3,1),2)
    if video_list[choosen_vid].duration - video_list[choosen_vid].t > gap:
        tempclip = VideoClip(video_list[choosen_vid].video_clip, video_list[choosen_vid].t, video_list[choosen_vid].t + gap)
        video_clip_list.append(tempclip)
        video_list[choosen_vid].t = video_list[choosen_vid].t + gap
    else:
        tempclip = VideoClip(video_list[choosen_vid].video_clip, video_list[choosen_vid].t, video_list[choosen_vid].duration)
        video_clip_list.append(tempclip)
        video_list[choosen_vid].t = video_list[choosen_vid].duration
        count_videos = count_videos - 1
        video_list.remove(video_list[choosen_vid])

for clip_temp in video_clip_list:
    print(clip_temp.video_clip_name)
    print(clip_temp.video_start)
    print(clip_temp.video_end)

finalVideoClip = VideoFileClip(video_clip_list[0].video_clip_name).subclip(video_clip_list[0].video_start,video_clip_list[0].video_end).resize((1280,720))

i = 1
while i < len(video_clip_list):
    final_video_temp = VideoFileClip(video_clip_list[i].video_clip_name).subclip(video_clip_list[i].video_start,video_clip_list[i].video_end).resize((1280,720))
    finalVideoClip = concatenate_videoclips([finalVideoClip , final_video_temp])
    i = i + 1

finalVideoClip.write_videofile("random_mashup.mp4")
