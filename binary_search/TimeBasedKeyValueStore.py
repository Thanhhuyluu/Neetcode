# https://neetcode.io/problems/time-based-key-value-store/question?list=neetcode150

class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [] 
        if self.dict[key] and self.dict[key][-1][1] == timestamp:
            self.dict[key][-1][0] = value
        else:
            self.dict[key].append([value, timestamp])



    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        values = self.dict[key] 
        for i in range(len(values)-1, -1, -1):
            if values[i][1] <= timestamp:
                return values[i][0]
        return ""

timemap = TimeMap()
timemap.set("alice", "happy", 1)
print(timemap.get("alice",1))
