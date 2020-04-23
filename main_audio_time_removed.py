from hashlib import sha1
import numpy as np
from pydub import AudioSegment
import fingerprint
import warnings
import json
warnings.filterwarnings("ignore")
import work
import sys

filename = "~/VMERGE/audio.mp3"



def audio_main(video_list):
    file_file = open(sys.argv[1] + "/mashup/audio_names.txt", "r")
    line = file_file.readline()
    list_videos = []
    while line:
        line = line.rstrip()
        list_videos.append(line)
        line = file_file.readline()


    list_time = []
    for vid_name in list_videos:
        for vid in video_list:
            if vid.video_clip == vid_name:
                list_time.append(vid.start_time*1000)

    list_time = list_time[1:]

    print("INSIDE AUDIO")
    print(list_videos)
    print(list_time)
    i = 1
    final_audio_temp = AudioSegment.from_file(list_videos[0], "mp4")
    # final_audio = final_audio_temp[:list_time[0]]
    final_audio = final_audio_temp[:(list_time[0] +1000)]

    while i < list_time.__len__():
        audio_file = AudioSegment.from_file(list_videos[i], "mp4")
        # final_audio = final_audio + audio_file[:list_time[i]]
        final_audio = final_audio.append(audio_file[:(list_time[i]+1000)], crossfade=1000)
        i = i + 1

    audio_file = AudioSegment.from_file(list_videos[i], "mp4")
    # final_audio = final_audio + audio_file
    final_audio = final_audio.append(audio_file, crossfade=1000)
    final_audio.export(sys.argv[1] + "/mashup/mashup.mp3", format="mp3")
    return
