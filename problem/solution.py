from InputParser import InputParser
from CacheManager import CacheManager

def process_file(filename):
    parser = InputParser()
    parser.parse("in/" + filename + ".in")
    manager = CacheManager()
    manager.videos = parser.getVideos()
    manager.caches = parser.getCaches()
    manager.endpoints = parser.getEndPoints()
    manager.requests = parser.getRequests()
    manager.FillCaches()

    outputstring = manager.OutputString()
    outputfile = open("out/" + filename + ".out", 'w')
    outputfile.write(outputstring)

if __name__ == "__main__":
    files = ["me_at_the_zoo", "kittens", "trending_today", "videos_worth_spreading"]
    files = ["videos_worth_spreading"]
    for file in files:
        print("starting file: "+file)
        process_file(file)

