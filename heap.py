import heapq

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]

heapq.heapify(data)
print(data)
"""
first child: 2*i+1
second child: 2*i+2
find parent: (i-1)/2 (using integer division)
using the `data` list:
    1
   /  \
  1    17
 /\   /  \
2  2  65  43

and so on...
"""

# Get element with highest priority
# (heapq is a min heap by default)
print(heapq.heappop(data))
# `heappop()` calls `heapify()` and `pop()`
print(data)

# `heappush()` calls `append()` and `heapify`
heapq.heappush(data, 2)

print(data)

# There isn't a built-in way to use a max heap
# One way to do this is to invert the numbers
data = [-x for x in data]
heapq.heapify(data)
print(data)

# Or, we can use an undocumented function `_heapify_max()`
data = [-x for x in data]
heapq._heapify_max(data)
print(data)
print(heapq._heappop_max(data))

# The best way to get a max heap is to create your own
# data structure

# You can also merge lists and heapify them
l1 = [10, 20, 30, 40, 50]
l2 = [15, 25, 35, 45, 55]
l3 = list(heapq.merge(l1, l2))
print(l3)

# nsmallest and nlargest -> Return a list with the n
# largest/smallest elements from the dataset defined by `iterable`
print(heapq.nlargest(3, l3))
print(heapq.nsmallest(3, l3))
