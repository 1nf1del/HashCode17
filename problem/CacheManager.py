class CacheManager:
    def __init__(self, printing=False):
        self.videos = list()
        self.caches = list()
        self.endpoints = list()
        self.requests = list()
        self.printing = printing

    def FillCaches(self):
        self.fillAlgo5()

    def fillAlgo1(self):
        self.requests.sort(key=lambda req: req.number, reverse=True)
        for request in self.requests:
            endpoint = request.endpoint
            video = request.video
            if self.printing:
                print("Requests:{0!s} video:{0!s} EP:{0!s}".format(request.number, video.id, endpoint.id))
            for (cache, latency) in endpoint.caches:
                if cache.put(video):
                    if self.printing:
                        print("Put in cache:{0!s} latency:{0!s}ms".format(cache.id, latency))
                    break

    def fillAlgo3(self):
        self.requests.sort(key=lambda req:req.number*(req.endpoint.maxdiff())/req.video.size,reverse=True)
        for request in self.requests:
            endpoint = request.endpoint
            video = request.video
            for (cache, latency) in endpoint.caches:
                cache.put(video)
                break


    def fillAlgo4(self):
        self.endpoints.sort(key=lambda ep: ep.score(), reverse=True)
        self.requests.sort(key=lambda req: req.number, reverse=True)
        for ep in self.endpoints:
            for request in self.requests:
                if request.endpoint == ep:
                    video = request.video
                    for (cache, latency) in ep.caches:
                        if cache.put(video):
                            break


    def fillAlgo5(self):
        self.endpoints.sort(key=lambda ep: ep.score(), reverse=True)
        self.requests.sort(key=lambda req: req.number, reverse=True)
        for ep in self.endpoints:
            for request in ep.requests:
                video = request.video
                already_present = False
                for (cache, latency) in ep.caches:
                    if video in cache.videos:
                        already_present = True
                if not already_present:
                    for (cache, latency) in ep.caches:
                        if cache.put(video):
                            break


    def OutputString(self):
        outputstr =""
        cache_count = 0
        for cache in self.caches:
            if len(cache.videos) > 0:
                cache_count += 1
                cache_line = str(cache.id) + " "
                for vid in cache.videos:
                    cache_line += str(vid.id) + " "
                outputstr += cache_line[:-1] + '\n'

        outputstr = str(cache_count) + '\n' + outputstr

        return outputstr
