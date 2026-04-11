class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp =defaultdict(list)

        for i in  strs:
            a=sorted(i)
            
            mp[str(a)].append(i)

        return list(mp.values())
