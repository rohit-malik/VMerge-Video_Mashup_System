class Video:
    def __init__(self, vid, start, end, ql):
        self.video_clip = vid
        self.start_time = start
        self.end_time = end
        self.quality = ql
        self.audio_quality = 0
