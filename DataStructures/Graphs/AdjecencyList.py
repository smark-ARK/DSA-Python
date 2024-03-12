class Vertex:
    def __init__(self, key) -> None:
        self.key = key
        self.neighbors = {}

    def get_key(self):
        return self.key

    def add_neighbor(self, vertex, weight=0):
        self.neighbors[vertex] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def __str__(self) -> str:
        return (
            f"Vertex {self.key} connects to -> {[key for key, val in self.neighbors]}"
        )


class Graph:
    def __init__(self) -> None:
        self.vertices = {}

    def get_vertices(self):
        return self.vertices.keys()

    def get_vertex(self, key) -> Vertex | None:
        return self.vertices[key]

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if not from_vertex in self.vertices:
            self.add_vertex(from_vertex)
        if not to_vertex in self.vertices:
            self.add_vertex(to_vertex)
        return self.get_vertex(from_vertex).add_neighbor(
            self.get_vertex(to_vertex), weight
        )
