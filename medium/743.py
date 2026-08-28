class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        q, t, adj = [(0,k)], {}, collections.defaultdict(list)
        for u,v, w in times:
            adj[u].append((v,w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time+w, v))
        return max(t.values()) if len(t) == n else -1
        