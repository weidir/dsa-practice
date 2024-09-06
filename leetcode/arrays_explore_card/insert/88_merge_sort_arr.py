from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        temp = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                temp.append(nums2[j])
                j += 1
            elif nums1[i] == nums2[j]:
                temp.append(nums1[i])
                temp.append(nums2[j])
                i += 1
                j += 1
        
        if i < m:
            temp.extend(nums1[i:])
        
        elif j < n:
            temp.extend(nums2[j:])
        
        nums1[:] = temp[:m+n]
    
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2[:n]

        nums1.sort()
        

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol = Solution()
    sol.merge2(nums1, m, nums2, n)
    print(nums1)
        