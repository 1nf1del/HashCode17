class Cache:
    def __init__(self,size):
        self.size = int(size)
        self.videos = list()
        self.free = self.size

    def put(self,video):
        if self.free >= video.size:
            self.videos.append(video)
            self.free -= video.size
            return True
        else:
            return False
