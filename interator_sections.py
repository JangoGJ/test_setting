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