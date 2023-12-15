class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        s = len(paths)
        print(paths[s - 1][len(paths[s - 1]) - 1])
        graph = {}

        for i in range(len(paths)):
            for city in paths[i]:
                if (city not in graph):
                    graph[city] = paths[i]
                for item in paths[i]:
                    if (item not in graph[city]):
                        graph[city].append(item)

        print(graph)
        return (graph)
    
Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])