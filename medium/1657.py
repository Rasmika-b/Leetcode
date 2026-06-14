class Solution(object):
    def closeStrings(self, word1, word2):
        count1, count2 = Counter(word1), Counter(word2)
        occur1 = sorted(count1.values())
        occur2 = sorted(count2.values())
        set1 = set(word1)
        set2 = set(word2)
        if occur1 == occur2 and set1 == set2:
            return True
        return False
        