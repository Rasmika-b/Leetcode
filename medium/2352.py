class Solution(object):
    def equalPairs(self, grid):
        pair = 0
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] = rows[tuple(row)] + 1
        for col in zip(*grid):
            pair = pair + rows[col]
        return pair
        