class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        arr=[]
        high = max(candies)
        for i in candies:
            if i+extraCandies >= high:
                arr.append(True)
            else:
                arr.append(False)
        return arr