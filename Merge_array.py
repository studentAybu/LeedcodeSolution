class Solution:
    def merge(self, nums1, m, nums2, n):
        numsMarge = [0] * (m + n)
        i, j, k = 0, 0, 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                numsMarge[k] = nums1[i]
                i += 1
            else:
                numsMarge[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            numsMarge[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            numsMarge[k] = nums2[j]
            j += 1
            k += 1

        for index in range(m + n):
            nums1[index] = numsMarge[index]
