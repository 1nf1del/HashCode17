from Video import Video
from EndPoint import EndPoint
from Cache import Cache
from Request import Request

class InputParser:
    def __init__(self):
        self.videoList = list()
        self.cacheList = list()
        self.requestList = list()
        self.endPointList = list()

    def getVideos(self):
        return self.videoList

    def getCaches(self):
        return self.cacheList

    def getRequests(self):
        return self.requestList

    def getEndPoints(self):
        return self.endPointList

    def parse(self,filename):
        inputfile = open(filename, 'r')
        firstline = inputfile.readline()
        param = firstline[:-1].split(' ')
        num_videos, num_endpoints, num_descriptions, num_caches, capacity = int(param[0]), int(param[1]), int(param[2]), int(param[3]), int(param[4])
        videoline = inputfile.readline()
        videos = videoline[:-1].split(' ')

        video_count = 0
        for size in videos:
            vid = Video(id=video_count, size=int(size))
            video_count += 1
            self.videoList.append(vid)

        for i in range(num_caches):
            cache = Cache(i, int(capacity))
            self.cacheList.append(cache)

        ep_count = 0
        for endpoint in range(num_endpoints):
            ep_line = inputfile.readline()[:-1]
            ep_line = ep_line.split(' ')
            datacenter_latency = int(ep_line[0])
            cache_count = int(ep_line[1])
            ep = EndPoint(ep_count, datacenter_latency)
            for cache in range(cache_count):
                cache_line = inputfile.readline()[:-1]
                cache_line = cache_line.split(' ')
                cache_id = int(cache_line[0])
                cache_latency = int(cache_line[1])
                ep.addCache(self.cacheList[cache_id], int(cache_latency))
            ep.sortCaches()
            self.endPointList.append(ep)
            ep_count += 1


        for i in range(num_descriptions):
            request_line = inputfile.readline()[:-1]
            request_line = request_line.split(' ')
            id_vid, id_ep, num= int(request_line[0]), int(request_line[1]), int(request_line[2])
            req = Request(self.videoList[id_vid],self.endPointList[id_ep],num)
            self.endPointList[id_ep].addRequest(req)
            self.requestList.append(req)



