def manhattan_distance(state, goal):
    total_distance = 0
    for tile in range(1, 9):
        current_index = state.index(tile)
        goal_index = goal.index(tile)

        current_row = current_index // 3
        current_col = current_index % 3

        goal_row = goal_index //3 
        goal_col = goal_index % 3

        distance = abs(current_row - goal_row) + abs (current_col -  goal_col)
        total_distance += distance
    return total_distance

inittial_state =  [7, 2, 4, 5, 0, 6, 8, 3, 1]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
heuristic_value = manhattan_distance(inittial_state, goal_state)
print(f"Heuristic value:{heuristic_value}")