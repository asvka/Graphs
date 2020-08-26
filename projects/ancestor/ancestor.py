from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Write a function that, given the dataset and the ID of an individual in the dataset,
    # returns their earliest known ancestor – the one at the farthest distance from the input individual.
    # If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
    # If the input individual has no parents, the function should return -1.

    # How can I utilize previous code/utils? DFS?
    graph = Graph()

    # iterate through ancestors and add
    for v1, v2 in ancestors:
        graph.add_vertex(v1)
        graph.add_vertex(v2)

    # Iterate, add edges
    for v1, v2 in ancestors:
        graph.add_edge(v1, v2)

    # target vertex
    current_vertex = None

    longest = 1

    for vertex in graph.vertices:
        path = graph.dfs(vertex, starting_node)

        if path:
            print(path)

            if len(path) > longest:
                longest = len(path)
                current_vertex = vertex

        elif not path and longest == 1:
            current_vertex = -1

    return current_vertex
