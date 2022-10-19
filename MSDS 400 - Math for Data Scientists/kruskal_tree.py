# This is a copy/paste of the Node and Graph class from the Graph Theory Notebook.
# The kruskal method on the Graph class is the only thing added here.
import string


class Node(object):
    '''
    This is a class that represents a node. The functions of a class are called methods. Instantiations of this class
    will create objects that have access to the methods.

    Each method begins with an argument of "self" which lets the methos know which object it belongs to.

    For the Node object, we care about the name of the node and a dictionary naming the adjacent nodes. The adjacent
    dictionary keys will be the name's of adjacent nodes and the value will be the weight of that edge.
    '''

    def __init__(self, name):
        # The init method is magic python method that get's called when an object is instantiated.
        self.name = name  # Take the name given at instantiation and assign it to the object
        self.adjacent = {}  # When we create the node, we don't know about any adjacent nodes. Create a placeholder

    def __str__(self):
        # When printing a node, format it like this:
        return "Node {}: {}".format(self.name, self.adjacent)

    def __repr__(self):
        # When representing this object, use the str method
        return self.__str__()


class Graph(object):
    '''
    This class represents a graph. The graph is consists of a collection of nodes.
    '''

    def __init__(self, adjacency_matrix=None):
        '''
        When the graph is instantiated it will not know about any of its member nodes. There is an optional
        `adjacency_matrix` argument that defaults to None. If an adjacency_matrix is provided, then we can
        create the member nodes, their relationships, and add them to this graph.
        '''
        self.nodes = {}
        if adjacency_matrix:
            # We were provided an adjacency matrix
            self._create_member_nodes_from_adjacency_matrix(adjacency_matrix)

    def __str__(self):
        return '\n'.join([str(n) for n in self.nodes.values()])

    def __repr__(self):
        return self.__str__()

    def _create_member_nodes_from_adjacency_matrix(self, adjacency_matrix):
        # A preceeding underscore indicates a method that is only called within the class.
        # Create nodes and weights from an adjacency matrix (list of lists) and assign them to this graph
        letters = list(string.ascii_lowercase)  # Get a list of letters to assign to the nodes we create
        needed_letters = len(adjacency_matrix)
        if needed_letters > len(letters):
            # Give the user an error that the input matrix is too large to have
            raise ValueError(
                "The matrix is too large to create from 26 letters. Please manually assign names to nodes and then add them to the graph.")

        for i, row in enumerate(adjacency_matrix):  # get an index of the row and the contentx of the row
            letter_name = letters[i]
            node = Node(letter_name)
            for j, column_value in enumerate(row):
                if column_value != 0:  # There is an adjacent node here
                    adjacent_letter_name = letters[j]
                    node.adjacent[adjacent_letter_name] = column_value
            self.nodes[letter_name] = node

    def get_distance_of_path(self, path):
        # Given a list of node names within the graph, find its distance using the node adjacency measures
        distance = 0
        for i, node_name in enumerate(path[:-1]):
            # Gets the index and node name for each in the path except for the last one
            this_node = self.nodes[node_name]
            next_node = self.nodes[path[i + 1]]
            distance += this_node.adjacent[next_node.name]  # Get the distance from this_node to next node

        return distance

    def find_all_paths_between(self, a, b, path=None):
        if not path:
            # No path list provided, create one
            path = []

        path = path + [a]  # Add a to the path

        if a == b:  # This is a path to itself, at the end of a path
            return [path]
        if a not in self.nodes:  # a could not be found in the graph
            return []
        paths = []
        for node in self.nodes[a].adjacent:  # look to adjacent nodes of a
            if node not in path:
                newpaths = self.find_all_paths_between(node, b, path)  # Recursivly go down another level
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def shortest_path(self, a, b):
        # Get the distance of each weighted path and return the shortest
        all_paths = self.find_all_paths_between(a, b)

        if not all_paths:
            return []

        # The shortest path will be the first path in the list
        shortest_path = None
        shortest_distance = None

        for path in all_paths:
            p_distance = self.get_distance_of_path(path)
            if not shortest_distance or p_distance < shortest_distance:
                # This path is shorter
                shortest_path = path
                shortest_distance = p_distance

        return shortest_path

    def is_tree(self):
        # returns True if the graph is a tree, otherwise False

        node_names = list(self.nodes.keys())
        first = node_names[0]  # Make sure the first node has a path to all other nodes

        for node in node_names:
            if node == first:
                continue  # Don't compare it against itself
            if not self.find_all_paths_between(first, node):
                return False  # No path was found between first and node, this must not be a tree

        return True

    def kruskal(self):
        # Find the minimum cost spanning tree on the graph using Kruskal's algorithm

        # Loop through the graph to get a deduplicated list of edges
        unique_edge_lenghts = dict()
        for node, connections in self.nodes.items():
            for connected, edge_length in connections.adjacent.items():
                alpha_edge = sorted([node, connected])

                edge_name = "-".join(alpha_edge)  # keeps nodes alphabetical to dedupe
                unique_edge_lenghts[edge_name] = edge_length

        # This sorts the edges by their lengths desc
        sorted_unique_edge_lengths = dict(sorted(unique_edge_lenghts.items(), key=lambda x: x[1]))

        # proceed through the sorted list and add the edge if it contains a new node.
        selected_nodes = set()
        selected_edges = list()
        for edge in sorted_unique_edge_lengths.keys():
            a, b = edge.split('-')
            if a in selected_nodes and b in selected_nodes:
                continue  # No circuits here
            selected_nodes.add(a)
            selected_nodes.add(b)
            selected_edges.append(edge)

        return selected_edges

matrix = [
    #P   L    R    D    M
    [0,  34,  42, 38, 33],  # P
    [34,  0,  40, 31, 25],  # L
    [42,  40,  0,  27, 32],  # R
    [38, 31, 27,  0, 28],  # D
    [33, 25, 32, 28, 0],  # M
]

g = Graph(matrix)

print(g)
print(f"The selected graph edges for the minimum tree is {g.kruskal()}")