class Graph:
    def __init__(self, nodes: int) -> None:
        self.size = nodes
        self.edges = 0
        self.matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

    def __str__(self) -> str:
        res = ""
        for i in range(self.size):
            res += f"{i}: "
            for j in self.matrix[i]:
                res += f" {j} "
            res += "\n"
        return res

    def add_edge(self, v, u):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
        self.edges += 1


test = Graph(4)
test.add_edge(0, 1)
test.add_edge(2, 1)
test.add_edge(0, 3)
test.add_edge(1, 3)
print(test)
