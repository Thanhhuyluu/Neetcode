# https://neetcode.io/problems/median-of-two-sorted-arrays/question?list=neetcode150
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merge_array = []
        while (i <= len(nums1) -1) and (j <= len(nums2) -1):
            if nums1[i] < nums2[j]:
                merge_array.append(nums1[i])
                i +=1
            else:
                merge_array.append(nums2[j])
                j +=1
        while i <= len(nums1) -1:
            merge_array.append(nums1[i])
            i +=1
        while j <= len(nums2) -1:
            merge_array.append(nums2[j])
            j +=1
        if len(merge_array) % 2 == 0:
            mid =int((len(merge_array)-1) / 2)
            return float((merge_array[mid] + merge_array[mid+1]) /2)
        else:
            return merge_array[int((len(merge_array)-1)/2)] 


solution = Solution()
print(solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3]))
print(solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4]))
