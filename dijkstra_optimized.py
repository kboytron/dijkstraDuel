import heapq 


def readGraph(path):
    graph = {}
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            node = int(parts[0])
            edges = []
            for edge in parts[1:]:
                dest, weight = map(int, edge.split(','))
                edges.append((dest, weight))
            graph[node] = edges
    return graph

def dijkstra(graph, source):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    pq = [(0, source)]  
    
    visited = set()
    
    while pq:
        current, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))
    
    return distances

graph = readGraph('testcase.txt')
source = 1  
distances = dijkstra(graph, source)

for node in sorted(distances):
    print(f"Shortest distance from node {source} to node {node} is {distances[node]}")

