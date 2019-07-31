import unittest
import util


class UtilitiesTest(unittest.TestCase):
    def test_string_to_tuple(self):
        """ Ensures the util.string_to_tuple function returns tuple representations
            of corresponding string input.
        """
        cases = {
            "(2,3,4)": (2, 3, 4),
            "(2,3)": (2, 3),
        }
        for test_input, expected_output in cases.items():
            actual_output = util.string_to_tuple(test_input)
            assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output}"

    def test_file_to_graph(self):
        """ Ensures the util.file_to_graph function returns the correct graph object
            when given a filepath to graph data.
        """
        graph = util.file_to_graph("graph_data.txt")

        # Ensure it reads the first line of file properly
        assert graph.directional == False

        # Ensure the vertices are what we expect
        vertices = graph.vertices.keys()
        assert len(vertices) == 4
        assert 1 in vertices
        assert 2 in vertices
        assert 3 in vertices
        assert 4 in vertices

        # Ensure the edges are what we expect
        assert graph.edges == [
            (1, 2, 10),
            (1, 4, 5),
            (2, 3, 5),
            (2, 4, 7)
        ]
