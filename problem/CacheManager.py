class CacheManager:
    def __init__(self):
        self.videos = list()
        self.caches = list()
        self.endpoints = list()
        self.requests = list()

    def FillCaches(self):
        self.requests.sort(key=lambda req:req.number, reverse=True)
        for request in self.requests:
            endpoint = request.endpoint
            video = request.video
            for (cache,latency) in endpoint.caches:
                if cache.put(video):
                    break



