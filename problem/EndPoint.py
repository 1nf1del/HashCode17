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
            diff += abs(self.datacenter_latency - lat)
            diff += abs(self.datacenter_latency**2 - lat**2)
        score = 0
        for request in self.requests:
            score += request.number
        score =score* diff / len(self.caches)
        return score


    def maxdiff(self):
        if self.caches:
            maxdiff = self.datacenter_latency - self.caches[0][1]
        else:
            maxdiff = 0
        return maxdiff

    def diff(self,cache):
        latency = self.datacenter_latency
        for i in range(len(self.caches)):
            if self.caches[i][0] == cache:
                latency = self.caches[i][1]
        return self.datacenter_latency - latency
