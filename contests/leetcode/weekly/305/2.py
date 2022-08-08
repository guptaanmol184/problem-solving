from collections import defaultdict
from typing import *

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = set(restricted)

        edge_dict = defaultdict(list)
        for x, y in edges:
            edge_dict[x].append(y)
            edge_dict[y].append(x)

        visited = set()
        def dfs(node, edge_dict) -> int:
                if node in res or node in visited:
                    return 0
                else:
                    visited.add(node)
                    s = 1
                    for a in edge_dict[node]:
                            s += dfs(a, edge_dict)
                    return s

        return dfs(0, edge_dict)


s = Solution() 
out = s.reachableNodes(7,[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5])
print(out)
        
out = s.reachableNodes(7,[[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,2,1])
print(out)