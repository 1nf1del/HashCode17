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
