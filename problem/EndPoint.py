class EndPoint:
    def __init__(self, datacenter_latency):
        self.caches = dict()
        self.datacenter_latency = datacenter_latency


    def addCache(self,id,latency):
        self.caches[id] = latency