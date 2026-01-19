import copy

def find_zero(grid):
    for r in range(3):
        for c in range(3):
            if(grid[r][c] == 0):
                return r, c;
    return None

def generate_neighbors(current_state):
    neighbors = []
    zero_row, zero_col = find_zero(current_state)

    moves = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    for dr, dc, move_name in moves:
       
        
        new_row = zero_row + dr
        new_col = zero_col + dc

        if 0<=new_row <3 and 0<=new_col<3:

            new_state = copy.deepcopy(current_state)

            val_to_swap = new_state[new_row][new_col]
            new_state[new_row][new_col] = 0
            new_state[zero_row][zero_col] = val_to_swap

            neighbors.append((new_state, move_name))

    return neighbors
current_state = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]
print(f"Current State: ")
for item in current_state:
    print(item)
print("-----------")
next_move = generate_neighbors(current_state)

print(f"Total moves: {len(next_move)}:\n")
for state, name in next_move:
    print(f"Move: {name} \n")
    for row in state:
        print(row)
    print("-----------")