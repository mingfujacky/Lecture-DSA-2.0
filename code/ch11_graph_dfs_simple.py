graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"],
}


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}

    while len(stack) > 0:
        vertex = stack.pop()  # DFS uses stack (LIFO), so we pop from the end
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent


parent = DFS(graph, "A")
print(parent)
