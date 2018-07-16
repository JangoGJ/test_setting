# A test for interitor section in python.
class CapitalIterable:
    def __init__(self, string):
        self.string = string
    def __iter__(self):
        return CapitalIterator(self.string)
class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0
    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word
    def __iter__(self):
        return self

iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

for i in iterable:
    print(i)

input_strings = ['1', '5', '28', '131', '3']
output_integers = []
for num in input_strings:
    output_integers.append(int(num))
print(output_integers)

input_strings = ['1', '5', '28', '131', '3']
output_integers =[int(num) for num in input_strings]
print(output_integers)

output_ints = [int(n) for n in input_strings if len(n) < 3]
print(output_ints)

def tally():
    score = 0
    while True:
        increment = yield score
        score += increment
white_sox = tally()
blue_jays = tally()
next(white_sox)

next(blue_jays)

white_sox.send(3)

blue_jays.send(2)

white_sox.send(2)

blue_jays.send(4)

import re
def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex = yield match.groups()[0]
def get_serials(filename):
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        bus = matcher.send('(sd \S+) {}.*'.format(re.escape(device)))
        serial = matcher.send('{} \(SERIAL=([^)]*)\)'.format(bus))
        yield serial
        device = matcher.send(ERROR_RE)
for serial_number in get_serials('EXAMPLE_LOG.log'):
    print(serial_number)