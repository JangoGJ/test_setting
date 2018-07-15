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

pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
search_string = "some.user@example.com"
match = re.match(pattern, search_string)
if match:
    domain = match.groups()[0]
    print(domain)

