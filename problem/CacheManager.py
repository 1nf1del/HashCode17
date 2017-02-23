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
                    print("")
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






