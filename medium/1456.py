class Solution(object):
    def maxVowels(self, s, k):
        a = set('aeiouAEIOU')
        curr = 0
        for i in range(k):
            if s[i] in a:
                curr = curr+1
        best = curr
        for r in range(k, len(s)):
            if s[r] in a:
                curr = curr+1
            if s[r-k] in a:
                curr = curr-1
            best = max(best, curr)
            if best == k:
                return k
        return best

