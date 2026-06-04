def has_cyclic(graph,node,visited,parent):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            if has_cyclic(graph,neighbour,visited,node):
                return True
        elif neighbour!=parent:
            return True
    return False
graph={
    0:[1,2],
    1:[0,2],
    2:[0,1,3],
    3:[2]
}
visited=set()
cycle_found=False
for node in graph:
    if node not in visited:
        if has_cyclic(graph,node,visited,-1):
            cycle_found=True
            break
if cycle_found:
    print("Cycle Detected")
else:
    print("No cycle found")