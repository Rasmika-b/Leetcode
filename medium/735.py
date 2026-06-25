class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                last = stack.pop()
                if last > -i:
                    stack.append(last)
                    break
                elif last == -i:
                    break
            else:
                stack.append(i)
        return stack

