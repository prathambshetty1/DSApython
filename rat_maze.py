def is_safe(maze,x,y,n):
    return 0 <=x<n and 0<=y<n and maze[x][y]==1
def solve_maze_util(maze,x,y,solution,n):
    if x==n-1 and y==n-1:
        solution[x][y]=1
        return True
    if is_safe(maze,x,y,n):
        solution[x][y]=1
        if solve_maze_util(maze,x,y+1,solution,n):
            return True
        if solve_maze_util(maze,x+1,y,solution,n):
            return True
        solution[x][y]=0
        return False
    return False
def solve_maze(maze):
    n=len(maze)
    solution=[[0]*n for _ in range(n)]
    if solve_maze_util(maze,0,0,solution,n):
        for row in solution:
            print(row)
    else:
        print("No solution exists!!")

maze=[
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
]
solve_maze(maze)