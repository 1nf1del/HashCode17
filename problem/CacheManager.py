class CacheManager:
    def __init__(self, printing=False):
        self.videos = list()
        self.caches = list()
        self.endpoints = list()
        self.requests = list()
        self.printing = printing

    def FillCaches(self):
        self.fillAlgo3()


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
        self.requests.sort(key=lambda req:req.number*(req.endpoint.maxdiff()),reverse=True)
        for request in self.requests:
            endpoint = request.endpoint
            video = request.video
            for (cache, latency) in endpoint.caches:
                cache.put(video)
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
