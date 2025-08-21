class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in range(0,len(digits)):
            s+=str(digits[i])
        s=list(str(int(s)+1))
        arr=[]
        for i in range(0,len(s)):
            arr.append(int(s[i]))
        return arr
        

sol=Solution()
res=sol.plusOne([1,2,3])

