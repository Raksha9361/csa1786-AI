from collections import deque

# Function to print the current state
def print_state(state):
    print(f"Jug 1: {state[0]} liters, Jug 2: {state[1]} liters")

# Function to check if the current state is visited
def is_visited(visited, state):
    return state in visited

# BFS approach to solve the water jug problem
def water_jug_problem(x, y, z):
    # Initial state: both jugs are empty
    initial_state = (0, 0)
    
    # Queue to perform BFS
    queue = deque([(0, 0)])
    
    # Set to keep track of visited states
    visited = set()
    visited.add(initial_state)
    
    # Perform BFS
    while queue:
        state = queue.popleft()
        print_state(state)
        
        # If we reached the goal state, return
        if state[0] == z or state[1] == z:
            print(f"Found the solution: Jug 1: {state[0]} liters, Jug 2: {state[1]} liters")
            return
        
        # Generate all possible states and add them to the queue
        next_states = [
            # Fill Jug 1
            (x, state[1]),
            # Fill Jug 2
            (state[0], y),
            # Empty Jug 1
            (0, state[1]),
            # Empty Jug 2
            (state[0], 0),
            # Pour water from Jug 1 to Jug 2
            (state[0] - min(state[0], y - state[1]), state[1] + min(state[0], y - state[1])),
            # Pour water from Jug 2 to Jug 1
            (state[0] + min(state[1], x - state[0]), state[1] - min(state[1], x - state[0])),
        ]
        
        # Add valid states to the queue
        for next_state in next_states:
            if not is_visited(visited, next_state):
                visited.add(next_state)
                queue.append(next_state)
    
    print("No solution exists.")

# Example usage
def solve():
    x = 4  # Capacity of Jug 1
    y = 3  # Capacity of Jug 2
    z = 2  # Desired amount of water
    water_jug_problem(x, y, z)

# Run the solution
solve()
