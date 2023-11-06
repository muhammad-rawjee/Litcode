from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        count_elem = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count_elem[num] = 1 + count_elem.get(num, 0)
        
        # Fill buckets
        for n,v in count_elem.items():
            buckets[v].append(n)
        
        # return buckets

        
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                res.append(number)
                if len(res) == k:
                    return res


ali = Solution()
some_res = ali.topKFrequent([1,1,1,2,2,3], 2)
print(some_res)



