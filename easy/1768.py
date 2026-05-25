class Solution(object):
    def mergeAlternately(self, word1, word2):
        word = []
        i = 0
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                word.append(word1[i])
            if i<len(word2):
                word.append(word2[i])
            i = i+1
        return ''.join(word)