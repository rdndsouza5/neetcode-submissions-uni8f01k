class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            table = [0]*26
            for i in s:
                table[ord(i)-ord('a')]+=1
            res[tuple(table)].append(s)
        return [v for v in res.values()]