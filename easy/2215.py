class Solution(object):
    def findDifference(self, nums1, nums2):
        a = set(nums1)
        b = set(nums2)
        n, m = set(), set()

        for a in nums1:
            if a not in nums2:
                n.add(a)
        
        for b in nums2:
            if b not in nums1:
                m.add(b)
        
        return [list(n), list(m)]
        