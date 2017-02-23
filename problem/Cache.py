class Cache:
    def __init__(self,size):
        self.size = size
        self.videos = list()
        self.free = self.size