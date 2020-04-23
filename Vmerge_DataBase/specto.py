import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pydub import AudioSegment
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import (generate_binary_structure,
                                      iterate_structure, binary_erosion)
import hashlib
from operator import itemgetter

IDX_FREQ_I = 0
IDX_TIME_J = 1
PEAK_NEIGHBORHOOD_SIZE = 20

######################################################################
# Sampling rate, related to the Nyquist conditions, which affects
# the range frequencies we can detect.
DEFAULT_FS = 44100

######################################################################
# Size of the FFT window, affects frequency granularity
DEFAULT_WINDOW_SIZE = 4096

######################################################################
# Ratio by which each sequential window overlaps the last and the
# next window. Higher overlap will allow a higher granularity of offset
# matching, but potentially more fingerprints.
DEFAULT_OVERLAP_RATIO = 0.5

######################################################################
# Degree to which a fingerprint can be paired with its neighbors --
# higher will cause more fingerprints, but potentially better accuracy.
DEFAULT_FAN_VALUE = 15

######################################################################
# Minimum amplitude in spectrogram in order to be considered a peak.
# This can be raised to reduce number of fingerprints, but can negatively
# affect accuracy.
DEFAULT_AMP_MIN = 10

threshold = 5
frame_rate = 44100

def fingerprint(channel_samples, Fs=DEFAULT_FS,
                wsize=DEFAULT_WINDOW_SIZE,
                wratio=DEFAULT_OVERLAP_RATIO,
                fan_value=DEFAULT_FAN_VALUE,
                amp_min=DEFAULT_AMP_MIN):
    """
    FFT the channel, log transform output, find local maxima, then return
    locally sensitive hashes.
    """
    # FFT the signal and extract frequency components
    arr2D = mlab.specgram(
        channel_samples,
        NFFT=wsize,
        Fs=Fs,
        window=mlab.window_hanning,
        noverlap=int(wsize * wratio))[0]

    # apply log transform since specgram() returns linear array
    arr2D = 10 * np.log10(arr2D)
    arr2D[arr2D == -np.inf] = 0  # replace infs with zeros

    # find local maxima
    local_maxima = get_2D_peaks(arr2D, plot=True, amp_min=amp_min)

    return local_maxima


def get_2D_peaks(arr2D, plot=False, amp_min=DEFAULT_AMP_MIN):
    # http://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.morphol$
    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, PEAK_NEIGHBORHOOD_SIZE)

    # find local maxima using our fliter shape
    local_max = maximum_filter(arr2D, footprint=neighborhood) == arr2D
    background = (arr2D == 0)
    eroded_background = binary_erosion(background, structure=neighborhood,
                                       border_value=1)

    # Boolean mask of arr2D with True at peaks
    detected_peaks = local_max ^ eroded_background

    # extract peaks
    amps = arr2D[detected_peaks]
    j, i = np.where(detected_peaks)
    # filter peaks
    amps = amps.flatten()
    peaks = zip(i, j, amps)
    peaks_filtered = [x for x in peaks if x[2] > amp_min]  # freq, time, amp

    # get indices for frequency and time
    frequency_idx = [x[1] for x in peaks_filtered]
    time_idx = [x[0] for x in peaks_filtered]
    return zip(time_idx, frequency_idx)

    # if plot:
    #     # scatter of the peaks
    #     fig, ax = plt.subplots()
    #     ax.set_axis_off()
    #
    #     ax.imshow(arr2D)
    #     ax.scatter(time_idx, frequency_idx)
    #     ax.set_xlabel('Time')
    #     ax.set_ylabel('Frequency')
    #     # ax.set_title("Spectrogram")
    #     plt.gca().invert_yaxis()
    #     plt.show()
    #     fig.savefig("Figure_2.png")

def check_overlap(filename1, filename2):
    # filename1 = "1.mp3"
    # filename2 = "2.mp3"


    audio1 = AudioSegment.from_file(filename1, "mp4")
    audio2 = AudioSegment.from_file(filename2, "mp4")
    frame_rate = audio1.frame_rate
    # print(frame_rate)
    data1 = np.fromstring(audio1._data, np.int16)
    data2 = np.fromstring(audio2._data, np.int16)

    channels1 = []
    for chn in xrange(audio1.channels):
        channels1.append(data1[chn::audio1.channels])

    channels2 = []
    for chn in xrange(audio2.channels):
        channels2.append(data2[chn::audio2.channels])

    arr2D_1 = fingerprint(channels1[0])

    arr2D_2 = fingerprint(channels2[0])

    arr2D_1_sorted = sorted(arr2D_1, key = lambda element : element[0])
    arr2D_2_sorted = sorted(arr2D_2, key = lambda element : element[0])
    output = get_match(arr2D_1_sorted, arr2D_2_sorted)
    # print(output)
    return output

def get_match(res1, res2):
    l = {}
    for tup in res2:
        for tu in res1:
            if tu[1] == tup[1]:
                if (tu[0] - tup[0]) in l:
                    l[tu[0] - tup[0]] = l[tu[0] - tup[0]] + 1
                else:
                    l[tu[0] - tup[0]] = 1

    maxi = 0
    max_index = 0
    for key in l:
        if l[key] > maxi:
            maxi = l[key]
            max_index = key
    match_seconds = (2048*max_index)/float(frame_rate)
    # print(match_seconds)

    maxi_second = 0
    max_index_second = 0
    for key in l:
        if l[key] > maxi_second and key!=max_index:
            maxi_second = l[key]
            max_index_second = key
    match_seconds_second = (2048*max_index_second)/float(frame_rate)
    print("Best-match: " + str(maxi) + " Time: " + str(match_seconds))
    print("Second-best-match: " + str(maxi_second) + " Time: " + str(match_seconds_second))
    if abs(match_seconds - match_seconds_second) < 0.12:
        return (check_match_correctness(res1, res2, max_index, max_index_second,maxi,1), match_seconds)
    return (check_match_correctness(res1, res2, max_index, max_index_second,maxi,0), match_seconds)



def find_max_diff(list_time):
    index = 1
    max_diff = 0
    while index < len(list_time):
        diff = list_time[index] - list_time[index-1]
        if diff > max_diff:
            max_diff = diff
        index = index + 1
    return max_diff

def find_avg_diff(list_time):
    index = 1
    avg_diff = 0.0
    while index < len(list_time):
        avg_diff = avg_diff + list_time[index] - list_time[index-1]
        index = index + 1
    if len(list_time) > 1:
        avg_diff = avg_diff/(len(list_time)-1)
    return avg_diff

def check_match_correctness(res1, res2, best_match, second_best_match, num_matches, time_diff):
    audio_1_best_match = []
    audio_2_best_match = []
    audio_1_second_best_match = []
    audio_2_second_best_match = []
    for tup in res2:
        for tu in res1:
            if tu[1] == tup[1]:
                if (tu[0] - tup[0]) == best_match:
                    audio_1_best_match.append(tu[0])
                    audio_2_best_match.append(tup[0])
                elif (tu[0] - tup[0]) == second_best_match:
                    audio_1_second_best_match.append(tu[0])
                    audio_2_second_best_match.append(tup[0])
    diff_1_best = find_max_diff(audio_1_best_match)
    diff_1_second_best = find_max_diff(audio_1_second_best_match)
    diff_2_best = find_max_diff(audio_2_best_match)
    diff_2_second_best = find_max_diff(audio_2_second_best_match)
    diff_1_best_avg = find_avg_diff(audio_1_best_match)
    diff_1_second_best_avg = find_avg_diff(audio_1_second_best_match)
    # print(audio_1_best_match)
    # print(diff_1_best)
    # print(audio_1_second_best_match)
    # print(diff_1_second_best)
    # print(audio_2_best_match)
    # print(diff_2_best)
    # print(audio_2_second_best_match)
    # print(diff_2_second_best)
    print(diff_1_best_avg)
    print(diff_1_second_best_avg)
    if time_diff == 1 and num_matches > 5 and diff_1_best_avg < 100:
        return 1
    if diff_1_best_avg == 0:
        return 0
    if num_matches > 10 and diff_1_best_avg < 20:
        return 1
    if num_matches <=2 and time_diff !=1:
        return 0
    if (diff_1_second_best_avg/diff_1_best_avg) > threshold and diff_1_best_avg < 6:
        return 1
    elif diff_1_best_avg < 50 and time_diff==1:
        return 1
    else:
        return 0


# plt.plot(arr2D_1)
# plt.plot(arr2D_2)
# fig, ax = plt.subplots()
# ax.set_axis_off()
# ax.imshow(arr2D_1)

# plt.gca().invert_yaxis()
# plt.show()
