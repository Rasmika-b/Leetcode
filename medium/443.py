class Solution(object):
    def compress(self, chars):
        write=0
        i=0
        while i<len(chars):
            letter=chars[i]
            count = 0
            while i<len(chars) and chars[i]==letter:
                count= count+1
                i=i+1
            chars[write]=letter
            write=write+1

            if count>1:
                for c in str(count):
                    chars[write]=c
                    write=write+1
        return write


        
        