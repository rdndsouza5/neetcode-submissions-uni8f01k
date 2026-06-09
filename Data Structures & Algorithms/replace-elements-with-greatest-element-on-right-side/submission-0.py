class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        def dfs(i):
            if i == len(arr)-1:
                tmp = arr[i]
                arr[i] = -1
                return tmp
            tmp = arr[i]
            arr[i]= dfs(i+1)
            return max(arr[i], tmp)

        dfs(0)
        
    
        return arr