# https://leetcode.com/problems/mose-common-word/

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ['hit']

import re
import collections

words = [
    word for word in 
    re.sub(r'[^\w]', ' ', paragraph).lower().split() # 따옴표 등을 공백으로 바꿔주는 re
    if word not in banned
    ]

counter = collections.Counter(words)

print(counter.most_common(1)[0][0])