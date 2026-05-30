class Solution(object):
    def reverseVowels(self, s):
        chars = list(s)
        vowel = set('aeiouAEIOU')
        l = 0
        r = len(s)-1
        while l<r:
            while l<r and chars[l] not in vowel:
                l = l+1
            while l<r and chars[r] not in vowel:
                r = r-1
            
            chars[l], chars[r] = chars[r], chars[l]
            l = l+1
            r = r-1
        
        return ''.join(chars)

        