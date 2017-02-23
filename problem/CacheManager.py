class CacheManager:
    def __init__(self):
        self.videos = list()
        self.caches = list()
        self.endpoints = list()
        self.requests = list()

    def FillCaches(self):
        self.requests.sort(key=lambda req: req.number, reverse=True)
        for request in self.requests:
            endpoint = request.endpoint
            video = request.video
            print("Requests:{0!s} video:{0!s} EP:{0!s}".format(request.number, video.id, endpoint.id))
            for (cache, latency) in endpoint.caches:
                if cache.put(video):
                    print("Put in cache:{0!s} latency:{0!s}ms".format(cache.id, latency))
                    break
