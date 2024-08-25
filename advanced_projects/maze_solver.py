# Curses module helps to change various outputs in terminal rather than printing various output
import curses
from curses import wrapper
import queue 
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"] ]
    
# Define the function to print the maze
def print_maze(maze, stdscr, path=[]):
    BLUE= curses.color_pair(1)
    RED= curses.color_pair(2)
    
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED) # Print maze at i row and j column with space of 2 in between column
            else:
                stdscr.addstr(i, j*2, value, BLUE)
            

# Find starting position O from maze
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value== start:
                return i, j
        
    return None

# define function to get neighbor that is valid for the maze
def find_neighbors(maze, row, col):
    neighbors= []
    
    if row>0: # UP
        neighbors.append((row-1, col))
    if row +1 < len(maze): # Down
        neighbors.append((row+1, col))
    if col>0: # Left
        neighbors.append((row, col-1))
    if col+1 < len(maze[0]): # Right
        neighbors.append((row, col+1))
    
    return neighbors
    
# Breadth First Search (BFS) Algorithm works by expanding from a start point and checking  neighbors through each 1 iterations. Using Queue module, the neighbor nodes are added to queue and the visited nodes are removed. This algorithms repeats the process until exit is found and the node that finds will be the shortest one.
def find_path(maze, stdscr):
    start= "O"
    end= "X"
    start_pos= find_start(maze, start)
    q= queue.Queue() # The first node goes and come out first
    q.put((start_pos, [start_pos])) # 1 paramter for current node, 2nd one for remembering the path when reached exit to print it out
    visited= set()
    
    while not q.empty():
        current_pos, path= q.get() # Get current pos and path
        row, col= current_pos # get the coordinates of current pos
        
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.5)
        stdscr.refresh()
        
        if maze[row][col]== end: # If we reach end X, return the path
            stdscr.addstr(row+2, 0, f"it is took {len(visited)} tries to find the solution")
            return path
            
        
        neighbors= find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited: # Removing visited neighbors
                continue
            
            r, c= neighbor
            if maze[r][c]== "#": # Remove obastacles from neighbors
                continue
            new_path= path+[neighbor]
            q.put((neighbor, new_path))# Add the neighnor and new path into queue
            visited.add(neighbor) # Add the new neighbor in visited set
            
        


# Define main function with input standard output screen
# Stdscr works as print function 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # intiliaze color parameters
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    find_path(maze, stdscr)
    
    stdscr.getch() # get character similar to input statement waiting for user to enter something before output
    
wrapper(main) # intialize the curse model
