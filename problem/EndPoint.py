from Cache import Cache
import operator

class EndPoint:
    def __init__(self, id, datacenter_latency):
        self.caches = list()
        self.id = id
        self.datacenter_latency = datacenter_latency
        self.requests = list()


    def addCache(self,cache,latency):
        self.caches.append((cache, latency))

    def addRequest(self, req):
        self.requests.append(req)

    def sortCaches(self):
        self.caches.sort(key=operator.itemgetter(1))

    def score(self):
        if not self.caches:
            return 0

        diff = 0
        for cache, lat in self.caches:
            diff += abs(self.datacenter_latency**2 - lat**2)

        score = 0
        for request in self.requests:
            score += request.number

        score =score* diff / len(self.caches)

        return score
