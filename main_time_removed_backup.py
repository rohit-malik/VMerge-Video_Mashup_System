import specto
from moviepy.editor import VideoFileClip, concatenate_videoclips
from datetime import datetime
from video import Video
from merge import Merge
from initialize import initialize
from pydub import AudioSegment
from pydub.utils import get_array_type
import array
import wave
import re
from main_audio import audio_main
from Mashup import Mashup
from audio_tuning import audio_making
import warnings
warnings.filterwarnings("ignore")
import work
import sys
import os
from os import listdir
from os.path import isfile, join
import main_audio_time_removed
import main_audio
from operator import itemgetter
import audio_quality

videoGap=5
lastCount=5

folder_name = sys.argv[1]
#file_names = os.listdir(folder_name)
file_names = [f for f in listdir(folder_name) if isfile(join(folder_name, f))]

print(file_names)


# HANDLING LARGE FILES BY DIVIDING THEM INTO SUBCLIPS

# new_file_names = []
#
# for i in range(len(file_names)):
#     file1 = folder_name + file_names[i]
#     audio1 = AudioSegment.from_file(file1, "mp4")
#     # audio1 = AudioSegment.from_file(file1)
#     if audio1.duration_seconds > 45:
#         video_file = VideoFileClip(file1)
#         file_name = file1.split('.')[0]
#         t = 0
#         count = 1
#         while t< audio1.duration_seconds:
#             if t+40 < audio1.duration_seconds:
#                 clip = video_file.subclip(t,t+40)
#                 clip.write_videofile(file_name + "_" + str(count) + "mp4")
#                 new_file_names.append(file_names[i].split('.')[0] + "_" + str(count) + "mp4")
#             else:
#                 clip = video_file.subclip(t,audio1.duration_seconds)
#                 clip.write_videofile(file_name + "_" + str(count) + "mp4")
#                 new_file_names.append(file_names[i].split('.')[0] + "_" + str(count) + "mp4")
#                 break
#             t = t + 30
#             count = count+ 1
#     else:
#         new_file_names.append(file_names[i])
#
# file_names = new_file_names
# print(file_names)

#########################




dict_matches = {}

for i in range(len(file_names)):
    j = i + 1
    while j < len(file_names):
        file1 = folder_name + file_names[i]
        file2 = folder_name + file_names[j]
        print(file1)
        print(file2)
        is_match , match_time = specto.check_overlap(file1, file2)
        if is_match > 0:
            print("Match")
            if file_names[i] in dict_matches:
                dict_matches[file_names[i]].append((file_names[j], match_time))
            else:
                dict_matches[file_names[i]] = [(file_names[j], match_time)]
            if file_names[j] in dict_matches:
                dict_matches[file_names[j]].append((file_names[i], -match_time))
            else:
                dict_matches[file_names[j]] = [(file_names[i], -match_time)]
        j = j + 1


print(dict_matches)


list_videos = []
for key in dict_matches:
    flag = 1
    for ele in dict_matches[key]:
        if ele[1] < 0:
            flag = 0
            break
    if flag == 1:
        start = key
        break

clip = VideoFileClip(folder_name + start)
video_clip = Video(folder_name + start, 0, clip.duration, 1)
list_videos.append(video_clip)

def initialise_list(current_ele):
    for ele in dict_matches[current_ele]:
        for vid in list_videos:
            if vid.video_clip == (folder_name + current_ele):
                start_current = vid.start_time
                end_current = vid.end_time
                break
        if ele[1] > 0:
            clip = VideoFileClip(folder_name + ele[0])
            start_time = start_current + ele[1]
            video_clip = Video(folder_name + ele[0], start_time,start_time + clip.duration, 1)
            list_videos.append(video_clip)

    max_end = 0
    for vid in list_videos:
            start_vid = vid.start_time
            end_vid = vid.end_time
            if end_vid > max_end:
                max_end = end_vid
                max_vid = vid.video_clip

    vid_name = max_vid.split('/')[-1]
    if vid_name != current_ele:
        initialise_list(vid_name)
    else:
        return


initialise_list(start)
print ("list_videos", list_videos)
list_videos.sort(key=lambda x: x.start_time)
i = 0
while i < list_videos.__len__():
    print(list_videos[i].video_clip)
    print(list_videos[i].start_time)
    print(list_videos[i].end_time)
    i = i + 1


result_previous = None
i = 1
starting = 1
while i < list_videos.__len__():
    flag = 0
    save = None

    if list_videos[i-1].end_time < list_videos[i].start_time:
        j = 0
        while j < i-1:
            if list_videos[j].end_time > list_videos[i].start_time:
                save = j
            j = j + 1
    else:
        flag = 1

    if flag == 0:
        if save is not None:
            filename1 = list_videos[save].video_clip
            save_object = list_videos[save]
            result_previous = None
        else:
            i = i + 1
            result_previous = None
            continue
    else:
        filename1 = list_videos[i-1].video_clip

    filename2 = list_videos[i].video_clip

    audio1 = AudioSegment.from_file(filename1, "mp4")
    audio2 = AudioSegment.from_file(filename2, "mp4")

    if result_previous is not None:
        result1_1 = result_previous
    else:
        result1_1 = work.work_audio(audio1, filename1)

    result2_2 = work.work_audio(audio2, filename2)
    result1 = result1_1[0]
    result2 = result2_2[0]
    frame_rate = result1_1[1]
    result_previous = result2_2

    res2 = list(result2)
    res2.sort(key=lambda x: x[1])
    res1 = list(result1)

    l = {}
    print("Length of result 1: " + str(len(res1)))
    print("Length of result 2: " + str(len(res2)))
    # for tup in res2:
    #     for tu in res1:
    #         if tu[0] == tup[0]:
    #             print("match ------")
    #             if (tu[1] - tup[1]) in l:
    #                 l[tu[1] - tup[1]] = l[tu[1] - tup[1]] + 1
    #             else:
    #                 l[tu[1] - tup[1]] = 1

    # Optimizing the above computation

    res1_sorted = sorted(res1,key=itemgetter(0))
    res2_sorted = sorted(res2,key=itemgetter(0))
    res1_count = 0
    res2_count = 0
    reset_state = 0
    new_state = 0
    print(len(res1_sorted))
    print(len(res2_sorted))
    print(res1_sorted[:20])
    print(res2_sorted[:20])
    last_rescount = 0
    while res1_count < len(res1_sorted):
        res2_count = last_rescount
        match_this = 0
        #print(res1_count)
        while res2_count < len(res2_sorted):
            #print(res2_sorted[res2_count][0])
            if res1_sorted[res1_count][0] == res2_sorted[res2_count][0]:
                last_rescount = res2_count
                #print("match------")
                if ( res1_sorted[res1_count][1] - res2_sorted[res2_count][1] ) in l:
                    l[ res1_sorted[res1_count][1] - res2_sorted[res2_count][1] ] =  l[ res1_sorted[res1_count][1] - res2_sorted[res2_count][1] ] + 1
                else:
                    l[ res1_sorted[res1_count][1] - res2_sorted[res2_count][1] ] = 1
                match_this = 1
            else:
                if match_this == 1:
                    break
            res2_count = res2_count + 1
        res1_count = res1_count + 1



    maxi = 0
    max_index = 0
    for key in l:
        if l[key] > maxi:
            maxi = l[key]
            max_index = key

    print(maxi)
    print(max_index)
    match_value = (2048 * max_index * 1000)/frame_rate
    print(match_value)
    match_value = match_value/1000.0
    #print(match_value)
    #print(abs(match_value))

    if maxi <= 5:
        print("No match")
        list_videos[i].start_time = list_videos[i-1].end_time
        list_videos[i].end_time = list_videos[i].start_time + audio2.duration_seconds
        i = i + 1
        continue

    if flag == 1:
        if match_value < 0:
            list_videos[i-1], list_videos[i] = list_videos[i], list_videos[i-1]
            if starting == 1:
                list_videos[i-1].start_time = 0
                list_videos[i-1].end_time = audio2.duration_seconds
                starting = 0

            list_videos[i].start_time = abs(match_value) + list_videos[i - 1].start_time
            list_videos[i].end_time = list_videos[i].start_time + audio1.duration_seconds
        else:
            list_videos[i].start_time = abs(match_value) + list_videos[i-1].start_time
            list_videos[i].end_time = list_videos[i].start_time + audio2.duration_seconds
    else:
        if match_value < 0:
            save_object.start_time = abs(match_value) + list_videos[i].start_time
            save_object.end_time = save_object.start_time + audio1.duration_seconds
        else:
            list_videos[i].start_time = match_value + save_object.start_time
            list_videos[i].end_time = list_videos[i].end_time + audio2.duration_seconds

    i = i + 1


#endTime = Tuple[1]
endTime = list_videos[0].end_time
i = 0
while i < list_videos.__len__():
    print(list_videos[i].video_clip)
    print(list_videos[i].start_time)
    print(list_videos[i].end_time)
    if list_videos[i].end_time > endTime:
        endTime = list_videos[i].end_time
    i = i + 1


print(endTime)
audio_making(list_videos, endTime)
#main_audio_time_removed.audio_main(list_videos)
main_audio.audio_main(list_videos)

endTime = list_videos[0].end_time
i = 0
print("Final Video Times: ---------------")
while i < list_videos.__len__():
    print(list_videos[i].video_clip)
    print(list_videos[i].start_time)
    print(list_videos[i].end_time)
    if list_videos[i].end_time > endTime:
        endTime = list_videos[i].end_time
    i = i + 1

#Merge(list_videos,endTime,videoGap,lastCount)

# Making audio based on quality
print("---------------------Making audio based on quality----------------")
audio_quality.select_audio(list_videos, endTime)
print("-------------------Audio Based on quality built---------------------")

mash = Mashup(list_videos,endTime,lastCount)
# mash.merge("/home/vmash/VMERGE/mashup")
# mash.mash("/home/vmash/VMERGE/mashup.mp3")

mash.merge(sys.argv[1] + "/mashup")
mash.mash(sys.argv[1] + "mashup/mashup.mp3")
