class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l= 1 
        r= n-2
        cache = {}
        def get(i):
            if i not in cache:
                val = mountainArr.get(i)
                cache[i] = val
                return val
            else:
                return cache[i]

        while l<=r:
            m = (l+r)//2
            left, mid, right = get(m-1), get(m), get(m+1)
            if left< mid< right:
                l=m+1
            elif left>mid>right:
                r = m-1
            else:
                print("broke")
                print(left,mid,right)
                break


        print(m)
        print(mid)
        def binaryLeftSearch(l, r):
            if l>r:
                return -1
            mid = (l+r)//2
            val = get(mid)
            if val == target:
                return mid
            if val< target:
                return binaryLeftSearch(mid+1, r)
            if val> target:
                return binaryLeftSearch(l, mid-1)
        
        def binaryRightSearch(l, r):
            print(l, r)
            if l>r:
                return -1
            mid = (l+r)//2
            val = get(mid)
            print("valr", val)
            if val == target:
                return mid
            if val < target:
                return binaryRightSearch(l, mid-1)
            if val> target:
                return binaryRightSearch(mid+1, r)

        val = binaryLeftSearch(0, m-1)
        if val!=-1:
            return val
        val = binaryRightSearch(m, n-1)
        if val!= -1:
            return val
        return -1 