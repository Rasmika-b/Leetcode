### Mathematics

1. Implement the power function pow(x, n) , which calculates the x raised to n i.e. x^n.

Brute Force Approach: o(n)
<pre>
def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    result = 1.0
    for _ in range(n):
        result *= x
    return result
</pre>
Optimized Approach - Iterative: o(logn)
<pre>
def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    result = 1.0
    while n > 0:
        if n % 2 == 1:      
            result *= x
        x *= x               
        n //= 2              
    return result
</pre>

### Bit Manipulation

1. Given two integers start and goal. Flip the minimum number of bits of start integer to convert it into goal integer.

Brute Force Approach: o(logn)
<pre>
def minBitFlips(start: int, goal: int) -> int:
  xor = start ^ goal
  count = 0
  while xor > 0:
    count += xor & 1
    xor >>= 1
  return count
</pre>
<pre>
def minBitFlips(start: int, goal: int) -> int:
  xor = start ^ goal
  binary_str = bin(xor)
  return binary_str.count('1')
</pre>

2. 

