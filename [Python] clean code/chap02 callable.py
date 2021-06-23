from collections import defaultdict

class CallCount:
    
    def __init__(self):
        self._counts = defaultdict(int)
    
    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]

cc = CallCount()
cc(1)
cc(1)
cc(1)
print(cc(1)) # 4
cc(2)
print(cc(2)) # 2