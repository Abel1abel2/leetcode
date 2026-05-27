class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size=float('inf')
        l=0
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                size=min(size,r-l+1)
                sum-=nums[l]
                l+=1
        size=0 if size==float('inf') else size
        return size
        