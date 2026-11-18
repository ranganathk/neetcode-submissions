class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keystore:
            self.keystore[key].append([value, timestamp])
        else:
            tup = [value, timestamp]
            self.keystore[key] = [tup]
        

    def get(self, key: str, timestamp: int) -> str:
        arrs = self.keystore.get(key, [])
        lt = 0
        rt = len(arrs) - 1
        
        res = ""

        while (lt <= rt):
            mid = (lt + rt) // 2
            if (arrs[mid][1] == timestamp):
                return arrs[mid][0]
            elif (arrs[mid][1] < timestamp):
                res = arrs[mid][0]
                lt = mid + 1
            else: 
                rt = mid - 1

        return res