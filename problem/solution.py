from InputParser import InputParser
from CacheManager import CacheManager

if __name__ == "__main__":
    parser = InputParser()
    parser.parse("in/me_at_the_zoo.in")
    manager = CacheManager()
    manager.videos = parser.getVideos()
    manager.caches = parser.getCaches()
    manager.endpoints = parser.getEndPoints()
    manager.requests = parser.getRequests()

    manager.FillCaches()
