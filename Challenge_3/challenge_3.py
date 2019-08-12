from util import file_to_graph
from sys import argv

if __name__ == '__main__':
    assert argv[1] is not None, "Data file path is required."
    assert argv[2] is not None, "'From' vertex is required."
    assert argv[3] is not None, "'To' vertex is required."

    graph = file_to_graph(argv[1])
    start, stop = argv[2], argv[3]

    if start.isdigit():
        start = int(start)
    if stop.isdigit():
        stop = int(stop)

    path = graph.depth_first_traversal(start, stop)
    has_path = 'TRUE' if stop in path else 'FALSE'

    print(f"There exists a path between vertex {start} and {stop}:", has_path)
    if path:
        path_between = path[:path.index(stop)+1]
        print("Vertices in the path:", ','.join(map(str, path_between)))
