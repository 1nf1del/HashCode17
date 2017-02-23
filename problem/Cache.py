class Cache:
    def __init__(self,id, size):
        self.id = id
        self.size = size
        self.videos = list()
        self.free = self.size
        self.videoscore = dict()

    def put(self,video):
        if self.free >= video.size and video not in self.videos:
            self.videos.append(video)
            self.free -= video.size
            return True
        else:
            return False

    def addvideoscore(self,video,endpoint,amount):
        if self.videoscore.has_key(video):
            self.videoscore[video]+=endpoint.diff(self)*amount
        else:
            self.videoscore[video] = endpoint.diff(self) * amount

    def getscore(self,video):
        return self.videoscore.get(video)