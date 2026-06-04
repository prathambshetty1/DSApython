from collections import deque
def bfs(city_map,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    print("Locations Visited:")
    while queue:
        location=queue.popleft()
        print(location,end=" ")
        for neighbor in city_map[location]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
city_map={
    "Airport": ["Mall","Railway Station"],
    "Mall": ["Hospital","College"],
    "Railway Station":["Bus Stand"],
    "Hospital":[],
    "College":[],
    "Bus Stand":[]
}
start_location=input("Enter starting location: ")
bfs(city_map,start_location)