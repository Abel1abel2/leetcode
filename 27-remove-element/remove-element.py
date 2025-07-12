class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        k=0
        while i<len(nums):
            if val==nums[i]:
                del nums[i]
                
            else:
                i+=1
                k+=1
        
        return k
nums=[3,2,2,3]
val=3
sol=Solution()
k=sol.removeElement(nums,val)
print(k)
print(nums)
     


        
     


        