class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            tmp = sorted(i)
            res[tuple(tmp)].append(i)
            

        return list(res.values())
            