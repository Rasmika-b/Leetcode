class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        indexs = [0]*numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indexs[a] += 1
        q = deque(i for i in range(numCourses) if indexs[i] == 0)
        count = 0
        while q:
            u = q.popleft()
            count += 1
            for v in adj[u]:
                indexs[v] -= 1
                if indexs[v] == 0:
                    q.append(v)
        return count == numCourses        
        