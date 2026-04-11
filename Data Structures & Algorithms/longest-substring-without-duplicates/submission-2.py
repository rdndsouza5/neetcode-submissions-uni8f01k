class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, maxCount=0,0
        count=0
        while l< len(s):
            j=l+count
            while j< len(s) and s[j] not in seen:
                seen.add(s[j])
                count+=1
                j+=1
            maxCount=max(count,maxCount)
            if j>=len(s):
                break

            while s[l]!=s[j] and l<j:
                seen.remove(s[l])
                count-=1
                l+=1
            seen.remove(s[l])
            l+=1
            count -=1
            
                
        return maxCount
