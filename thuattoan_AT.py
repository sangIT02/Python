graph = {
    'A':{"B":2,"C":4,"F":6},
    'B':{},
    "C":{"D":2,"E":8},
    "D":{"E":2},
    "E":{},
    "F":{"G":5,"H":1},
    "G":{},
    "H":{}
}


def print_path_and_cost(start, goal, parent, g):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    print("duong di: ", ' -> '.join(path))
    print("C(p) = ",g[goal])


def AT(graph, start, goals):
    MO = [start]
    g = {start: 0}
    DONG = []
    parent = {}
    while MO:
        min_cost = float('inf')
        n = None
        for vertex in MO:
            if vertex in g:
                cost = g[vertex]
            else:
                cost = float('inf')
            if cost < min_cost:
                min_cost = cost
                n =vertex
        if n in goals:
            print_path_and_cost(start, n, parent, g)
            return True
        MO.remove(n)
        DONG.append(n)
        for m in graph.get(n, {}):
            cost = graph[n][m]
            new_cost = g.get(n, float('inf')) + cost
            if m in parent and new_cost < g[m]:
                g[m] = new_cost
                parent[m] = n
            elif m not in MO and m not in DONG:
                g[m] = new_cost
                parent[m] = n
                MO.append(m)
    return False

start = "A"
goals = ["E", "H"]
AT(graph, start, goals)