class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for i in nums:
            count[i] = count.get(i,0) +1

        arr = []
        for n, cnt in count.items():
            arr.append([cnt,n])
        arr.sort()

        res = []
        i = -1
        while len(res) < k:
            res.append(arr[i][1])
            i-=1
        return res