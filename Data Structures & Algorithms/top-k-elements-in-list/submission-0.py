from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        a = sorted(((key, count) for key, count in counts.items()), key = lambda x: x[1], reverse = True)
        return list(map(lambda x: x[0], a[:k]))