class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        adj = defaultdict(list)
        for s, d in tickets:
            adj[s].append(d)

        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        if len(res) == len(tickets)+1:
            return res[::-1]
        return []