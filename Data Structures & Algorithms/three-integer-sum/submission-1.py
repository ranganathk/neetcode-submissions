class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hash_map:
                hash_map[nums[i]].append(i)
            hash_map[nums[i]] = [i]

        arr = []
        for j in range(n-1):
            for k in range(j+1, n):
                key = 0 - (nums[j] + nums[k])
                if key in hash_map:
                    for m in hash_map[key]:
                        if m != j and m != k:
                            arr.append([nums[j], nums[k], nums[m]])

        second_hash = {}
        for ar in arr:
            ar.sort()
            key = '-'.join(map(str, ar))
            second_hash[key] = ar

        result = []
        for a, b in second_hash.items():
            result.append(b)
        
        return result

