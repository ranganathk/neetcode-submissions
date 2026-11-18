class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        top_k = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)[:k]

        seconds = [sublist[0] for sublist in top_k]

        return seconds
        
