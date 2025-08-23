class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)):
            nums1.pop()
        for i in range(0,n):
            nums1.append(nums2[i])
        for i in range(0,len(nums1)):
            minIndex=i
            for j in range(i+1,len(nums1)):
                if nums1[minIndex]>nums1[j]:
                    minIndex=j
            nums1[minIndex],nums1[i]=nums1[i],nums1[minIndex]