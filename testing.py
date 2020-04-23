import warnings

from pydub import AudioSegment

import work

warnings.filterwarnings("ignore")


def get_fingerprint(filename):
    audio_part = AudioSegment.from_file(filename, "mp4")
    result_fingerprint = work.work_audio(audio_part, filename)
    result = result_fingerprint[0]
    frame_rate = result_fingerprint[1]
    resultant = list(result)
    return [resultant, frame_rate]


class VideoFile:
    def __init__(self, filename):
        self.fingerprint = None
        self.frame_rate = None
        self.name = filename


file_list = []
with open("File_names.txt") as f:
    for line in f:
        temp_file = VideoFile(line.strip())
        file_list.append(temp_file)


i = 0
while i < file_list.__len__():
    temp_fingerprint = get_fingerprint(file_list[i].name)
    file_list[i].fingerprint = temp_fingerprint[0]
    file_list[i].frame_rate = temp_fingerprint[1]
    i = i + 1


def get_match(fprint1, fprint2):
    l = {}
    for tup in fprint2:
        for tu in fprint1:
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

    print(maxi)
    print(max_index)
    match_value = (2048 * max_index * 1000) / file_list[i].frame_rate
    print(match_value)
    match_value = match_value / 1000.0
    # print(match_value)
    # print(abs(match_value))
    return [match_value, maxi]


file_object = open("testing_result.txt","w")
for i in range(0,file_list.__len__()):
    for j in range(i+1, file_list.__len__()):
        match = get_match(file_list[i].fingerprint, file_list[j].fingerprint)
        string_to_write = file_list[i].name + "\t" + file_list[j].name + "\t" + str(match[0]) + "\t" + str(match[1]) + "\n"
        file_object.write(string_to_write)

file_object.close()

