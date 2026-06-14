class Solution(object):
    def uniqueOccurrences(self, arr):
        count = defaultdict(int)
        for i in arr:
            count[i] = count[i]+1
        occur = list(count.values())
        return len(occur) == len(set(occur))