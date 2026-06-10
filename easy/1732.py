class Solution(object):
    def largestAltitude(self, gain):
        arr=[0, gain[0]]
        for i in range(len(gain)-1):
            j = gain[i]+gain[i+1]
            arr.append(j)
            gain[i+1]=j

        return max(arr)

        