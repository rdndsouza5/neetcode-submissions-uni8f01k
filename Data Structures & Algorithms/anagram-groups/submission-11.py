class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            sortedStr = sorted(s)
            hm[tuple(sortedStr)].append(s)
        
        res = []

        for v in hm.values():
            res.append(v)
        return res