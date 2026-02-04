from ch10_graph_list import GraphList
from pathlib import Path
def is_star_graph(graph):
    center_count = 0
    for vertex in range(graph.n):
        degree = len(graph.L[vertex])
        if degree == graph.n - 1:
            center_count += 1
        elif degree != 1:
            return False
    return center_count == 1

file_path = Path.cwd() / 'asset' / 'txt' / 'graph_star.txt'
candidate_graph = GraphList()
candidate_graph.read_file(file_path)
candidate_graph.print()
if is_star_graph(candidate_graph):
    print("The graph is a star graph.")
else:
    print("The graph is not a star graph.")