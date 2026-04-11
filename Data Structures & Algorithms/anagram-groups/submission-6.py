class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            tmp = sorted(i)
            if tuple(tmp) in res:
                res[tuple(tmp)].append(i)
            else:
                res[tuple(tmp)]=[i]

        return list(res.values())
            