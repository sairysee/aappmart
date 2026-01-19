class KnowledgeGraph:

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)
        self.graph[from_node].append(to_node)

    def __repr__(self):
        return str(self.graph)
