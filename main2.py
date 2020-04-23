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


#Important variables--------------------------
videoList = []
#endTime=0
videoGap=5
lastCount=5
#videoList contains the all Video objects


with open("File_names.txt") as f:
    for line in f:
        line2 = line.strip()
        videoList.append(line2)


num_videos = videoList.__len__()
i = 1
starting = 1
fingerprintlist = []
Matrix1 = [[0 for x in range(num_videos)] for y in range(num_videos)]
Matrix2 = [[0 for x in range(num_videos)] for y in range(num_videos)]

for i in range(0,videoList.__len__()):
    for j in range(i+1,videoList.__len__()):
        filename1 = videoList[i]

        filename2 = videoList[j]

        audio1 = AudioSegment.from_file(filename1, "mp4")
        audio2 = AudioSegment.from_file(filename2, "mp4")

        if fingerprintlist.__len__() > i:
            result1_1 = fingerprintlist[i]
        else:
            result1_1 = work.work_audio(audio1, filename1)
            fingerprintlist.append(result1_1)

        if fingerprintlist.__len__() > j:
            result2_2 = fingerprintlist[j]
        else:
            result2_2 = work.work_audio(audio2, filename2)
            fingerprintlist.append(result2_2)

        result1 = result1_1[0]
        result2 = result2_2[0]
        frame_rate = result1_1[1]

        res2 = list(result2)
        res2.sort(key=lambda x: x[1])
        res1 = list(result1)

        l = {}
        for tup in res2:
            for tu in res1:
                if tu[0] == tup[0]:
                    if (tu[1] - tup[1]) in l:
                        l[tu[1] - tup[1]] = l[tu[1] - tup[1]] + 1
                    else:
                        l[tu[1] - tup[1]] = 1

        maxi = 0
        max_index = 0
        for key in l:
            if l[key] > maxi:
                maxi = l[key]
                max_index = key

        #print(maxi)
        #print(max_index)
        match_value = (2048 * max_index * 1000)/frame_rate
        #print(match_value)
        match_value = match_value/1000.0
        #print(match_value)
        #print(abs(match_value))
        Matrix1[i][j] = maxi
        Matrix2[i][j] = match_value
        if maxi <= 5:
            print("No match")


#print(Matrix1)
#print(Matrix2)
for i in range(num_videos):
    for j in range(i+1,num_videos):
        print(videoList[i]+" "+videoList[j]+" "+str(Matrix1[i][j])+" "+str(Matrix2[i][j]))


#audio_making(list_videos, endTime)
#audio_main()
#Merge(list_videos,endTime,videoGap,lastCount)

#mash = Mashup(list_videos,endTime,lastCount)
#mash.merge("C:/Users/Nitin Malik/PycharmProjects/untitled5/mashup")
#mash.mash("C:/Users/Nitin Malik/PycharmProjects/untitled5/mashup.mp3")

"""
video1 = VideoFileClip("video3.flv").subclip(0,10)
video1.write_videofile("vid_test1.mp4")

video2 = VideoFileClip("video3.flv").subclip(7.5,16)
video2.write_videofile("vid_test2.mp4")

video3 = VideoFileClip("video3.flv").subclip(13,18)
video3.write_videofile("vid_test3.mp4")

check_list = []
object1 = Video("vid_test1.mp4",0,10,1)
object2 = Video("vid_test2.mp4",7,16,1)
object3 = Video("vid_test3.mp4",13,18,1)
check_list.append(object1)
check_list.append(object2)
check_list.append(object3)
endTime = 18
audio_making(check_list, endTime)





count = 1
final_clip = None
for vid in videoList:
    print(vid.video_clip)
    print(vid.start_time)
    print(vid.end_time)
    clip = VideoFileClip(vid.video_clip).resize((1280,720))
    if count ==1:
        final_clip = clip
    else:
        final_clip = concatenate_videoclips([final_clip , clip])
    count = 0

final_clip.write_videofile("testing_concat.mp4")
"""