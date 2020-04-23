from pydub import AudioSegment
import sys
sys.path.insert(1, '../')
import work

sound1 = AudioSegment.from_file("choolo1_1.mp3", "mp3")
sound2 = AudioSegment.from_file("choolo1_2.mp3", "mp3")

print(sound1.rms)
print(sound1.dBFS)
print(sound2.rms)
print(sound2.dBFS)

sound_unnormalized = sound1 + sound2
sound_unnormalized.export("unnormalized.mp3", "mp3")

sound2_changed = sound2.apply_gain(sound1.dBFS - sound2.dBFS)

sound_normalized = sound1 + sound2_changed
sound_normalized.export("normalized.mp3", "mp3")


filename1 = "choolo1_1.mp3"
filename2 = "choolo1_2.mp3"
audio1 = AudioSegment.from_file("choolo1_1.mp3", "mp3")
audio2 = AudioSegment.from_file("choolo1_2.mp3", "mp3")


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

print(maxi)
print(max_index)
match_value = (2048 * max_index * 1000)/frame_rate
print(match_value)

audio_unnormal = audio1[:10000] + audio2[10000-match_value:30000]
audio_unnormal.export("unnormal.mp3", "mp3")

audio_normal = audio1[:10000] + sound2_changed[10000-match_value:30000]
audio_normal.export("normal.mp3", "mp3")
