from collections import deque, defaultdict

def bfs(n, m, edges, s):
    g = defaultdict(list)
    for edge in edges:
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])
    
    visited = {s}
    res = {}
    level = 0
    queue = deque([s])
    import ipdb;ipdb.set_trace()
    while queue:
        curr = queue.popleft()
        level += 1
        for i in g[curr]:
            if i not in visited:
                res[i] = level * 6
                queue.append(i)
                visited.add(i)
                
    print(res)
bfs(5,3, [[5,3], [1,2], [1,3]], 1)
