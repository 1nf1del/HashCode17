from Cache import Cache
import operator

class EndPoint:
    def __init__(self, datacenter_latency):
        self.caches = list()
        self.datacenter_latency = datacenter_latency


    def addCache(self,id,latency):
        cache = Cache(id)
        self.caches.append((cache, latency))

    def sortCaches(self):
        self.caches.sort(key=operator.itemgetter(1))
