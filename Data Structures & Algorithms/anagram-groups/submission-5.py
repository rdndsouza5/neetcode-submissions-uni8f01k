class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            tmp = sorted(i)
            if tuple(tmp) in res:
                res[tuple(tmp)].append(i)
            else:
                res[tuple(tmp)]=[i]

        return [v for v in res.values()]
            