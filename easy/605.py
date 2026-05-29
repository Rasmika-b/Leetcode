class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                check_left = (i==0) or (flowerbed[i-1] == 0)
                check_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            
                if check_left is True and check_right is True:
                    flowerbed[i] = 1
                    n = n-1

            if n <= 0:
                return True
        
        return n <= 0
        
