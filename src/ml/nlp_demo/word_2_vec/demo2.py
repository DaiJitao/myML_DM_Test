

import collections

data = ["I", "I", "like", "you", "you", "you"]

print(collections.Counter(data)) #
print(collections.Counter(data).most_common(2))


print([ 1 if word in data[:-1]  else 0 for word in data])