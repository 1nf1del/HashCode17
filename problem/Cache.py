class Cache:
    def __init__(self,id, size):
        self.id = id
        self.size = size
        self.videos = list()
        self.free = self.size

    def put(self,video):
        if self.free >= video.size and video not in self.videos:
            self.videos.append(video)
            self.free -= video.size
            return True
        else:
            return False
