class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for a in strs:
            key = [0]*26
            for i in a:
                key[ord(i)-ord('a')]+=1
            ans[tuple(key)].append(a)
        return list(ans.values())