from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        bucketList = [[] for x in range(len(nums) + 1)]
        for number, count in counts.items():
            bucketList[count].append(number)

        res = []
        for x in bucketList[::-1]:
            for num in x:
                res.append(num)
                if len(res) == k:
                    return res