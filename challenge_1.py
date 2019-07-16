from graph import Graph


def graph_from_file(filepath):
    """ Returns a Graph instance using data from filepath's contents """
    with open(filepath) as f:
        lines = f.read().splitlines()
        edges = list(map(string_to_tuple, lines[2:]))

    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)

    return graph


def string_to_tuple(string):
    """ Turns a string into a tuple object """
    # Remove front and back parenthesis:
    string = string[1:-1]

    # Split remainder by commas:
    elements = string.split(',')

    # Handle type casting for integers:
    elements = map(lambda s: int(s) if s.isdigit() else s, elements)

    return tuple(elements)


if __name__ == '__main__':
    print(graph_from_file('graph_data.txt'))
    print(string_to_tuple("(1,2,3)"))
