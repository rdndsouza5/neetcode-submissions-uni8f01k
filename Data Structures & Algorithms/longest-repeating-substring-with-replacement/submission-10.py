class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0 
        for i in range(len(s)):
            char = s[i]
            tmp_k = k
            count = 0
            
            # Start from 'i' to include the first character in the count
            for j in range(i, len(s)):
                if s[j] != char:
                    if tmp_k > 0:
                        tmp_k -= 1
                    else:
                        # No more replacements left, stop this window
                        break
                
                # Increment the length of the valid segment found
                count += 1
            count += min(tmp_k,i)
            # Update the global maximum
            maxCount = max(count, maxCount)
        
        return maxCount