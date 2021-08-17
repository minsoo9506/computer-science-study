#  상위 k 빈도 요소
nums = [1,1,1,2,2,3]
k = 2

import collections

freq = collections.Counter(nums)
print(freq.most_common(2))
print(*freq.most_common(2))
print(zip(*freq.most_common(2)))
print(list(zip(*freq.most_common(2))))