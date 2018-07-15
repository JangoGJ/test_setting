import re
search_string = "hello world"
pattern = "hello world"
match = re.match(pattern, search_string)
if match:
    print("regex matches")

# import sys
# pattern = sys.argv[1]
# search_string = sys.argv[2]
# match = re.match(pattern, search_string)
# if match:
#     template = "'{}' matches pattern '{}'"
# else:
#     template = "'{}' does not match pattern '{}'"
# print(template.format(search_string, pattern))

# pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
# search_string = "some.user@example.com"
# match = re.match(pattern, search_string)
# if match:
#     domain = match.groups()[0]
#     print(domain)

from threading import Timer
import datetime
from urllib.request import urlopen
class UpdatedURL:
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()
    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()
    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()
    def __getstate__(self):
        new_state = self.__dict__.copy()
        if 'timer' in new_state:
            del new_state['timer']
        return new_state
    def __setstate__(self, data):
        self.__dict__ = data
        self.schedule()
u = UpdatedURL("http://news.yahoo.com/")
import pickle
serialized = pickle.dumps(u)

class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def full_name(self):
        return("{} {}".format(self.first, self.last))

c = Contact("John", "Smith")
x=json.dumps(c.__dict__)