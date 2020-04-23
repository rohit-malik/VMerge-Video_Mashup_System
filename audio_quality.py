from video import Video
from pydub import AudioSegment
import warnings
warnings.filterwarnings("ignore")
import sys
import random
from scipy import stats
import numpy as np

class AudioQuality:
    def __init__(self, aud, start, end, audio_quality):
        self.audio_clip = aud
        self.start_time = start
        self.end_time = end
        self.audio_quality = audio_quality

class AudioClips:
    def __init__(self, aud, start, end):
        self.audio_clip_name = aud
        self.audio_start = start
        self.audio_end = end

# audio_list = []
final_audio_clip_list = []

def assign_quality(audio_list):
    #Assign audio quality
    for i in range(0, len(audio_list)):
        # audio_list[i].audio_quality = random.choice([1, 2, 3, 4, 5])
        audio_clip = AudioSegment.from_file(audio_list[i].audio_clip, "mp4")
        audio_sample = np.array(audio_clip.get_array_of_samples())
        audio_list[i].audio_quality = abs(stats.signaltonoise(audio_sample, axis = 0, ddof = 0))
    for i in range(0, len(audio_list)):
        print("Audio Name: " + audio_list[i].audio_clip)
        print("Audio Quality: " + str(audio_list[i].audio_quality))
    return audio_list

def select_audio(video_list, endTime):
    audio_list = []
    for video_ele in video_list:
        audio_temp = AudioQuality(video_ele.video_clip, video_ele.start_time, video_ele.end_time, 0)
        audio_list.append(audio_temp)

    audio_list = assign_quality(audio_list)
    current_audio_list = []
    audio_list.sort(key=lambda x: x.start_time)
    current_audio_list.append(audio_list[0])
    t = 0
    while t < endTime - 1:
        print("Value of t:" + str(t))
        print(len(final_audio_clip_list))
        if len(current_audio_list) <= 0:
            for audio_temp in audio_list:
                if audio_temp.end_time > t and audio_temp.start_time < t:
                    current_audio_list.append(audio_temp)
            current_audio_list.sort(key=lambda x: x.audio_quality, reverse=True)
        audio_save = None
        for audio_temp in audio_list:
            if audio_temp.audio_quality > current_audio_list[0].audio_quality and audio_temp.start_time < current_audio_list[0].end_time and audio_temp.start_time > t:
                if audio_save is None:
                    audio_save = audio_temp
                else:
                    if audio_save.audio_quality < audio_temp.audio_quality:
                        audio_save = audio_temp

        if audio_save is not None:
            audio_temp_clip = AudioClips(current_audio_list[0].audio_clip, t - current_audio_list[0].start_time, audio_save.start_time - current_audio_list[0].start_time)
            final_audio_clip_list.append(audio_temp_clip)
            t = audio_save.start_time
            current_audio_list.insert(0, audio_save)
            while len(current_audio_list) > 1 and audio_save.end_time > current_audio_list[1].end_time:
                current_audio_list.pop(1)
        else:
            audio_temp_clip = AudioClips(current_audio_list[0].audio_clip, t - current_audio_list[0].start_time, current_audio_list[0].end_time - current_audio_list[0].start_time)
            final_audio_clip_list.append(audio_temp_clip)
            t = current_audio_list[0].end_time
            current_audio_list.pop(0)

    print(len(final_audio_clip_list))
    make_audio(final_audio_clip_list)


def make_audio(audio_clip_list):
    for clip_temp in audio_clip_list:
        print(clip_temp.audio_clip_name)
        print(clip_temp.audio_start)
        print(clip_temp.audio_end)
    final_audio_temp = AudioSegment.from_file(audio_clip_list[0].audio_clip_name, "mp4")
    final_audio = final_audio_temp[:audio_clip_list[0].audio_end*1000]

    i = 1
    while i < len(audio_clip_list):
        final_audio_temp = AudioSegment.from_file(audio_clip_list[i].audio_clip_name, "mp4")
        final_audio = final_audio + final_audio_temp[audio_clip_list[i].audio_start*1000: audio_clip_list[i].audio_end*1000]
        i = i + 1

    final_audio.export(sys.argv[1] + "/mashup/quality_audio_mashup.mp3", format="mp3")
