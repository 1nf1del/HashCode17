from Instances/Video import Video
from Instances/EndPoint import EndPoint
from Instances/Cache import Cache
from Instances/Request import Request

class InputParser:
    def __init__(self):
        self.videoList = list()
        self.cacheList = list()
        self.requestList = list()
        self.endPointList = list()

    def parse(self,filename):
        inputfile = open(filename, 'r')
        firstline = inputfile.readline()
        param = firstline[:-1].split(' ')
        num_videos, num_endpoints, num_descriptions, num_caches, capacity = int(param[0]), int(param[1]), int(param[2]), int(param[3]), int(param[4])
        videoline = inputfile.readline()
        videos = videoline[:-1].split(' ')

        for size in videos:
            vid = Video(size)
            self.videoList.append(vid)

        for i in range(num_caches):
            cache = Cache(capacity)
            self.cacheList.append(cache)



        for endpoint in num_endpoints:
            ep_line = inputfile.readline()[:-1]
            ep_line = ep_line.split(' ')
            datacenter_latency = ep_line[0]
            cache_count = ep_line[1]
            ep = EndPoint(datacenter_latency)
            for cache in cache_count:
                cache_line = inputfile.readline()[:-1]
                cache_line = cache_line.split(' ')
                cache_id = cache_line[0]
                cache_latency = cache_line[1]
                ep.addCache(cache_id, cache_latency)

            self.endPointList.append(ep)


        for i in range(num_descriptions):
            request_line = inputfile.readline()[:-1]
            request_line = request_line.split(' ')
            id_vid, id_ep, num= int(request_line[0]), int(request_line[1]), int(request_line[2])
            req = Request(id_vid,id_ep,num)
            self.requestList.append(req)


