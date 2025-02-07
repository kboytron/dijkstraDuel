def loadGraph(path):
    V = set()
    E = {}
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            node = int(parts[0])
            V.add(node)
            for edge in parts[1:]:
                dest, weight = map(int, edge.split(','))
                E[(node, dest)] = weight
    return V, E

def path(V, E, s):
    S = {s}
    p = {node: float('inf') for node in V}
    p[s] = 0
    
    while S != V:
        i, val = None, float('inf')
        for v in V - S:
            minV = min((p[u] + E.get((u, v), float('inf')) for u in S), default=float('inf'))
            if minV < val:
                i, val = v, minV
        if i is None:  
            break
        p[i] = val
        S.add(i)
    
    return p


file_path = 'testcase.txt' 
V, E = loadGraph(file_path)
source_node = 1

result = path(V, E, source_node)
print("Shortest distances from source node:")
for node, distance in result.items():
    if distance < float('inf'):
        print(f"Node {node}: Distance {distance}")
    else:
        print(f"Node {node}: Not reachable")
