from urllib.request import urlopen
from urllib.parse import urlparse
from queue import Queue
import re
import sys
LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")
# class LinkCollector:
#     def __init__(self, url):
#         self.url = "" + urlparse(url).netloc

#     def collect_links(self, path="/"):
#         full_url = self.url + path
#         page = str(urlopen(full_url).read())
#         links = LINK_REGEX.findall(page)
#         print(links)
# if __name__ == "__main__":
#     LinkCollector(sys.argv[1]).collect_links()

# def normalize_url(self, path, link):
#     if link.startswith("http://"):
#         return link
#     elif link.startswith("/"):
#         return self.url + link
#     else:
#         return self.url + path.rpartition('/')[0] + '/' + link

class LinkCollector:
    def __init__(self, url):
        # self.url = "http://+" + urlparse(url).netloc
        self.url = "http://%s" % urlparse(url).netloc
        self.collected_links = {}
        self.visited_links = set()

    def collect_links(self, path="/"):
        queue = Queue()
        queue.put(self.url)
        while not queue.empty():
            url = queue.get().rstrip('/')
            self.visited_links.add(url)
            page = str(urlopen(url).read())
            links = LINK_REGEX.findall(page)
            links = {self.normalize_url(urlparse(url).path, link) for link in links}
            self.collected_links[url] = links
            for link in links:
                self.collected_links.setdefault(link, set())
            unvisited_links = links.difference(self.visited_links)
            for link in unvisited_links:
                if link.startswith(self.url):
                    queue.put(link)
    def normalize_url(self, path, link):
        if link.startswith("http://"):
            return link.rstrip('/')
        elif link.startswith("/"):
            return self.url + link.rstrip('/')
        else:
            return self.url + path.rpartition('/')[0] + '/' + link.rstrip('/')
if __name__ == "__main__":
    collector = LinkCollector(sys.argv[1])
    collector.collect_links()
    for link, item in collector.collected_links.items():
        print("%s: %s" % (link, item))
        # full_url = self.url + path
        # self.visited_links.add(full_url)
        # page = str(urlopen(full_url).read())
        # links = LINK_REGEX.findall(page)
        # links = {self.normalize_url(path, link) for link in links}
        # self.collected_links[full_url] = links
        # for link in links:
        #     self.collected_links.setdefault(link, set())
        # # self.collected_links = links.union(self.collected_links)
        # unvisited_links = links.difference(self.visited_links)
        # print(links, self.visited_links,self.collected_links, unvisited_links)
        # for link in unvisited_links:
        #     if link.startswith(self.url):
        #         self.collect_links(urlparse(link).path)
#     def normalize_url(self, path, link):
#         if link.startswith("http://"):
#             return link
#         elif link.startswith("/"):
#             return self.url + link
#         else:
#             return self.url + path.rpartition('/')[0] + '/' + link


# if __name__ == "__main__":
#     collector = LinkCollector(sys.argv[1])
#     collector.collect_links()
#     for link, item in collector.collected_links.items():
#         print("{}: {}".format(link, item))

# if __name__ == "__main__":
#     collector = LinkCollector(sys.argv[1])
#     collector.collect_links()
#     for link in collector.collected_links:
#         print(link)