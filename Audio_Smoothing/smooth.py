from pydub import AudioSegment
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import (generate_binary_structure,
                                      iterate_structure, binary_erosion)
import hashlib
from operator import itemgetter

DX_FREQ_I = 0
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

######################################################################
# If True, will sort peaks temporally for fingerprinting;
# not sorting will cut down number of fingerprints, but potentially
# affect performance.
PEAK_SORT = True

######################################################################
# Number of bits to throw away from the front of the SHA1 hash in the
# fingerprint calculation. The more you throw away, the less storage, but
# potentially higher collisions and misclassifications when identifying songs.
FINGERPRINT_REDUCTION = 20
IDX_FREQ_I = 0
IDX_TIME_J = 1

######################################################################
# Thresholds on how close or far fingerprints can be in time in order
# to be paired as a fingerprint. If your max is too low, higher values of
# DEFAULT_FAN_VALUE may not perform as expected.
MIN_HASH_TIME_DELTA = 0
MAX_HASH_TIME_DELTA = 200


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

    # return local_maxima
    return generate_hashes(local_maxima, fan_value=fan_value)


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


def generate_hashes(peaks, fan_value=DEFAULT_FAN_VALUE):
    """
    Hash list structure:
       sha1_hash[0:20]    time_offset
    [(e05b341a9b77a51fd26, 32), ... ]
    """

    if PEAK_SORT:
        peaks.sort(key=itemgetter(1))

    for i in range(len(peaks)):
        for j in range(1, fan_value):
            if (i + j) < len(peaks):

                freq1 = peaks[i][IDX_FREQ_I]
                freq2 = peaks[i + j][IDX_FREQ_I]
                t1 = peaks[i][IDX_TIME_J]
                t2 = peaks[i + j][IDX_TIME_J]
                t_delta = t2 - t1

                if t_delta >= MIN_HASH_TIME_DELTA and t_delta <= MAX_HASH_TIME_DELTA:
                    h = hashlib.sha1(
                        "%s|%s|%s" % (str(freq1), str(freq2), str(t_delta)))
                    yield (h.hexdigest()[0:FINGERPRINT_REDUCTION], t1)


def work_audio(audiofile, filename):
    data = np.fromstring(audiofile._data, np.int16)

    channels = []
    for chn in xrange(audiofile.channels):
        channels.append(data[chn::audiofile.channels])

    fs = audiofile.frame_rate
    result = set()
    channel_amount = len(channels)

    for channeln, channel in enumerate(channels):
        # TODO: Remove prints or change them into optional logging.
        print("Fingerprinting channel %d/%d for %s" % (channeln + 1,
                                                       channel_amount,
                                                       filename))
        hashes = fingerprint(channel, Fs=fs)
        print("Finished channel %d/%d for %s" % (channeln + 1, channel_amount,
                                                 filename))
        result |= set(hashes)

    return [result, fs]

filename1 = "/home/vmash/VMERGE/Audio_Smoothing/vid1.mp4"
filename2 = "/home/vmash/VMERGE/Audio_Smoothing/vid2.mp4"

audio1 = AudioSegment.from_file(filename1, "mp4")
audio2 = AudioSegment.from_file(filename2, "mp4")

result1_1 = work_audio(audio1, filename1)
result2_2 = work_audio(audio2, filename2)

result1 = result1_1[0]
result2 = result2_2[0]
frame_rate = result1_1[1]

res2 = list(result2)
res2.sort(key=lambda x: x[1])
res1 = list(result1)

l = {}
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

audio_crossfade = audio1.append(audio2, crossfade=5000)

audio_crossfade.export("/home/vmash/VMERGE/Audio_Smoothing/mashed.mp3", format="mp3")
