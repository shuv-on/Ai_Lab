def find_position(grid, tile):
    for r in range(3):
        for c in range(3):
            if grid[r][c] == tile:
                return (r, c)
    return None        
def manhattan_distance(current_state, goal_state):
    total_distance = 0
    for tile in range(1, 9):
        pos_current = find_position(current_state, tile)
        pos_goal = find_position(goal_state, tile)

        row_diff = abs(pos_current[0] - pos_goal[0]) #pos_current[0] => tuple 0 index
        col_diff = abs(pos_current[1] - pos_goal[1]) #pos_current[1] => tuple 1 index

        distance = row_diff + col_diff
        total_distance += distance
    return total_distance

current_state = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
heuristic_value = manhattan_distance(current_state, goal_state)
print(f"Heuristic value: {heuristic_value}")