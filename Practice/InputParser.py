from Instances/Video import Video

class InputParser:
    def __init__(self):
        self.videolist = list()

    def parse(self,filename):
        inputfile = open(filename, 'r')
        firstline = inputfile.readline()
        print(firstline)
        param = firstline[:-1].split(' ')
        num_videos, num_endpoints, num_descriptions, num_caches, num_capacity = int(param[0]), int(param[1]), int(param[2]), int(param[3]), int(param[4])
        videoline = inputfile.readline()
        videos = videoline[:-1].split(' ')

        for size in videos:
            vid = Video(size)
            self.videolist.append(vid)

        for

        for endpoint in num_endpoints:
            ep_line = inputfile.readline()[:-1]
            ep_line = ep_line.split(' ')
            datacenter_latency = ep_line[0]
            cache_count = ep_line[1]
            for cache in cache_count:
                cache_line = inputfile.readline()[:-1]
                cache_line = cache_line.split(' ')
                cache_id = cache_line[0]
                cache_latency = cache_line[1]



