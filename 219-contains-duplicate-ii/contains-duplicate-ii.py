class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sub=set()
        for r in range(len(nums)):
            if r>k:
                sub.remove(nums[r-k-1])
            if nums[r] in sub:
                return True
            sub.add(nums[r])
        return False