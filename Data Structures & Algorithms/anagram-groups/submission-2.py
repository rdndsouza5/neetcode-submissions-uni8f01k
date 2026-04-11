class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap ={}
        for s in strs:
            # Convert sorted string into a tuple (to use as a key)
            a = tuple(sorted(s))
            # Add the original string to the list of anagrams in the hash map
            if a in hashMap:
                hashMap[a].append(s)
            else:
                hashMap[a] = [s]
        
        # Return all the lists of anagrams
        return list(hashMap.values())