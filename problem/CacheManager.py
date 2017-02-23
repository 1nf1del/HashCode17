class CacheManager:
    def __init__(self):
        self.videos = list()
        self.caches = list()
        self.endpoints = list()
        self.requests = list()

    def FillCaches(self):
        self.requests.sort(key=lambda req:req.number , reverse=True)
        for 

