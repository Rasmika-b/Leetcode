class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        l = list(freq.items())
        l.sort(key = lambda x: -x[1])
        words = [ch*n for ch, n in l]
        ans = ''.join(words)

        return ans
        