class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        while nums1 and nums2:
            if(nums1[0] > nums2[0]):
                ans.append(nums2.pop(0))
            else:
                ans.append(nums1.pop(0))
        while nums1:
            ans.append(nums1.pop(0))
        while nums2:
            ans.append(nums2.pop(0))
        n = len(ans)
        if n % 2 == 0:
            return (ans[n//2] + ans[n//2 - 1])/2
        else:
            return ans[n//2]
