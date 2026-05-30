class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        maxAvg=0
        for i in range(k):
            sum+=nums[i]
            maxAvg=sum/k
        for i in range(k,len(nums)):
            sum-=nums[i-k]
            sum+=nums[i]
            avg=sum/k
            maxAvg=max(maxAvg,avg)
        return maxAvg

        