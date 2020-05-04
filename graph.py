class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        self.distance = float("inf")
        self.previous_node = None

    def get_adjacent_nodes(self):
        nodes = [edge.node_to for edge in self.edges]

        return nodes

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        results = [None] * (self.get_max_node_value() + 1)
        for edge in self.edges:
            if results[edge.node_from.value]: 
                results[edge.node_from.value].append((edge.node_to.value, edge.value))
            else:
                results[edge.node_from.value] = [(edge.node_to.value, edge.value)]
        return results

    def get_max_node_value(self):
        return max([node.value for node in self.nodes])

    def get_node_with_value(self, value):
        return filter(lambda node: node.value == value, self.nodes)[0]


    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        adj_matrix = [[0] * (self.get_max_node_value() + 1) for _ in range(self.get_max_node_value())]
        for edge in self.edges:
            adj_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adj_matrix

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(205, 1, 4)
graph.insert_edge(103, 3, 4)
graph.insert_edge(102, 2, 4)
graph.insert_edge(102, 6, 7)

# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
# print graph.get_edge_list()
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
# print graph.get_adjacency_list()
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
# print graph.get_adjacency_matrix()

def extract_min(node_array):
    return min(node_array, key=lambda node: node.distance)

def dyjkstra(graph, start, end):
    start_node = graph.get_node_with_value(start)
    start_node.distance = 0
    current = start_node
    nodes_to_check = current.get_adjacent_nodes()
    while nodes_to_check:
        if current.value == end or current.distance == float("inf"):
            if current.value != end:
                return "No route found"
            chain_back = []
            while current.previous_node:
                chain_back.append(current.value)
                current = current.previous_node
            chain_back.append(current.value)
            return chain_back
        adjacent_edges = graph.get_adjacency_list()[current.value]
        # [(2, 100), (3, 101), (4, 205)]
        for edge in adjacent_edges:
            node = graph.get_node_with_value(edge[0])
            if current.distance + edge[1] < node.distance:
                node.distance = current.distance + edge[1]
                node.previous_node = current
                nodes_to_check.append(node)
        current.visited = True
        current = extract_min(nodes_to_check)
        nodes_to_check.remove(current)
    # print [(node.value, node.distance, node.previous_node, node.visited) for node in graph.nodes]

    # min_node = extract_min()

    # min_node_value, distances = extract_min(distances)
    # return distances, min_node_value

print(dyjkstra(graph, 1, 6))

