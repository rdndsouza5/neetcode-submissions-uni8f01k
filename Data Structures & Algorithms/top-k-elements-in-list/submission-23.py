class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num]  = 1 + count.get(num, 0)
        arr = [[] for i in range(len(nums)+1)]
        for n, cnt in count.items():
            arr[cnt].append(n)
        res = []
        print(arr)
        for i in range(len(arr)-1,-1,-1):
            for n in (arr[i]):
                res.append(n)
                if len(res)==k:
                    return res
