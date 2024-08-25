import numpy as np
import matplotlib.pyplot as plt
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Define the Maze structure using Reward Matrix
R = np.matrix([
    [-1, -1, -1, -1, 0, -1],   # Room 0 connections
    [-1, -1, -1, 0, -1, 100],  # Room 1 connections
    [-1, -1, -1, 0, -1, -1],   # Room 2 connections
    [-1, 0, 0, -1, 0, -1],     # Room 3 connections
    [0, -1, -1, 0, -1, 100],   # Room 4 connections
    [-1, 0, -1, -1, 0, 100]    # Room 5 (End location)
])

Q = np.matrix(np.zeros([6, 6]))  # Q Matrix initialized to zero
gamma = 0.8                      # Learning factor
alpha = 0.9                      # Learning rate
goal_state = 5                   # Fixed end location

def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act

def sample_next_action(available_actions_range):
    return int(np.random.choice(available_actions_range, 1))

def update_Q(current_state, action, gamma):
    max_index = np.where(Q[action, ] == np.max(Q[action, ]))[1]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    
    max_value = Q[action, max_index]
    Q[current_state, action] = R[current_state, action] + gamma * max_value

def train():
    for i in range(10000):
        current_state = np.random.randint(0, int(Q.shape[0]))
        available_act = available_actions(current_state)
        action = sample_next_action(available_act)
        update_Q(current_state, action, gamma)
    print("Training complete. Q matrix:")
    print(Q/np.max(Q) * 100)

def get_optimal_path(starting_location):
    current_state = starting_location
    steps = [current_state]
    
    while current_state != goal_state:
        next_step_index = np.where(Q[current_state, ] == np.max(Q[current_state, ]))[1]
        
        if next_step_index.shape[0] > 1:
            next_step_index = int(np.random.choice(next_step_index, size=1))
        else:
            next_step_index = int(next_step_index)
        
        steps.append(next_step_index)
        current_state = next_step_index
    
    return steps

def visualize_path(steps):
    fig, ax = plt.subplots()
    
    # Maze layout based on the provided image
    maze_layout = {
        0: (0, 2),
        1: (2, 2),
        2: (4, 2),
        3: (2, 1),
        4: (0, 0),
        5: (4, 1)
    }
    
    # Plot the rooms
    for room, (x, y) in maze_layout.items():
        ax.text(x, y, f"Room {room}", va='center', ha='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='black'))

    # Plot the connections
    connections = [(0, 4), (4, 1), (1, 3), (3, 2), (2, 5), (1, 5)]
    for (start, end) in connections:
        start_pos = maze_layout[start]
        end_pos = maze_layout[end]
        ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], 'k-', lw=2)

    # Highlight the optimal path
    for i in range(len(steps) - 1):
        start_pos = maze_layout[steps[i]]
        end_pos = maze_layout[steps[i + 1]]
        ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], 'r-', lw=3)
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

# Main execution
if __name__ == "__main__":
    train()
    starting_location = int(input("Enter the starting room (0-4): "))
    optimal_path = get_optimal_path(starting_location)
    print(f"Optimal Path: {'--> '.join(str(i) for i in optimal_path)}")
    visualize_path(optimal_path)