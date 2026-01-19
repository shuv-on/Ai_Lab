import heapq  # প্রায়োরিটি কিউ (সেরাটা আগে বের করার জন্য)
import copy   # বোর্ড কপি করার জন্য

# ১. আমাদের লক্ষ্য (Goal State)
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# --- সাহায্যকারী ফাংশন: বোর্ডের টাইলগুলোর পজিশন বের করা ---
def find_position(grid, tile):
    for r in range(3):
        for c in range(3):
            if grid[r][c] == tile:
                return (r, c)
    return None

# --- ২. হিউরিস্টিক ফাংশন (Manhattan Distance) ---
# এটা বলে দেয় গন্তব্য আর কত দূরে (h)
def manhattan_distance(current_state):
    distance = 0
    for r in range(3):
        for c in range(3):
            tile = current_state[r][c]
            if tile != 0:  # ০ বাদে বাকিদের দূরত্ব মাপব
                goal_r, goal_c = find_position(GOAL_STATE, tile)
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

# --- ৩. নেইবর জেনারেশন (Neighbor Generation) ---
# এটা সম্ভাব্য সব মুভ বা চাল তৈরি করে
def generate_neighbors(current_state):
    neighbors = []
    
    # ০ কোথায় আছে খুঁজে বের করি
    zero_pos = find_position(current_state, 0)
    zero_row, zero_col = zero_pos

    # ৪টি দিক: (row change, col change)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right

    for dr, dc in moves:
        new_row = zero_row + dr
        new_col = zero_col + dc

        # বাউন্ডারি চেক (বোর্ডের বাইরে যেন না যায়)
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = copy.deepcopy(current_state)
            
            # Swap (অদলবদল)
            new_state[zero_row][zero_col] = new_state[new_row][new_col]
            new_state[new_row][new_col] = 0
            
            neighbors.append(new_state)
            
    return neighbors

# --- লিস্টকে Tuple বানানোর ফাংশন (Visited সেটের জন্য) ---
# কারণ Python এ List কে সরাসরি Set এ রাখা যায় না
def to_tuple(grid):
    return tuple(tuple(row) for row in grid)

# --- ৪. মেইন A* অ্যালগরিদম ---
def solve_puzzle_astar(start_state):
    # Priority Queue তে আমরা রাখব: (f, g, board)
    # f = মোট খরচ (g + h)
    # g = শুরু থেকে কত কদম এসেছি
    priority_queue = []
    
    # শুরুর হিসাব
    g_start = 0
    h_start = manhattan_distance(start_state)
    f_start = g_start + h_start
    
    # কিউতে প্রথম স্টেট ঢুকালাম
    heapq.heappush(priority_queue, (f_start, g_start, start_state))
    
    # Visited Set (যাতে একই রাস্তায় গোলকধাঁধায় না পড়ি)
    visited = set()
    visited.add(to_tuple(start_state))

    print("Checking solutions... (Please wait)")
    nodes_checked = 0

    while priority_queue:
        # ১. সবচেয়ে কম f ওয়ালা বোর্ডটা বের করে আনি (Pop)
        current_f, current_g, current_board = heapq.heappop(priority_queue)
        nodes_checked += 1

        # ২. চেক করি: এটাই কি গোল?
        if current_board == GOAL_STATE:
            print("\n-----------------------------")
            print("🎉 Success! Solution Found!")
            print(f"Total Moves (g): {current_g}")
            print(f"Nodes Checked: {nodes_checked}")
            print("Final Board State:")
            for row in current_board:
                print(row)
            print("-----------------------------")
            return

        # ৩. প্রতিবেশীদের (Neighbors) জেনারেট করি
        for neighbor in generate_neighbors(current_board):
            neighbor_tuple = to_tuple(neighbor)

            # যদি এই বোর্ড আগে না দেখে থাকি
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                
                # নতুন g এবং h হিসাব করি
                new_g = current_g + 1
                new_h = manhattan_distance(neighbor)
                new_f = new_g + new_h  # A* এর মেইন সূত্র (f = g + h)
                
                # কিউতে যোগ করি
                heapq.heappush(priority_queue, (new_f, new_g, neighbor))

    print("No solution found!")

# --- ৫. রান করার জায়গা ---

# একটি কঠিন পাজল (Start State)
initial_board = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

print("Starting Board:")
for row in initial_board:
    print(row)

# ফাংশন কল
solve_puzzle_astar(initial_board)