from Cache import Cache
import operator

class EndPoint:
    def __init__(self, id, datacenter_latency):
        self.caches = list()
        self.id = id
        self.datacenter_latency = datacenter_latency


    def addCache(self,cache,latency):
        self.caches.append((cache, latency))

    def sortCaches(self):
        self.caches.sort(key=operator.itemgetter(1))

    def score(self):
        diff = 0
        for cache, lat in self.caches:
            diff += abs(self.datacenter_latency - lat)
