from collections import deque

class p8_board:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x   # 0 এর Row পজিশন
        self.y = y   # 0 এর Column পজিশন
        self.depth = depth # কত তম ধাপে আছি

def is_valid(x, y):
    # চেক করে নতুন পজিশন বোর্ডের ভেতরে আছে কিনা
    return 0 <= x < 3 and 0 <= y < 3

def is_goal(board):
    # আমাদের লক্ষ্য বা টার্গেট বোর্ড
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal

def bfs(start, x, y):
    queue = deque()
    # ১. শুরুর বোর্ডটি কিউ-তে যোগ করলাম
    queue.append(p8_board(start, x, y, 0))
    
    visited = set()
    # ১. শুরুর বোর্ডটি 'দেখা হয়েছে' (visited) তালিকায় রাখলাম
    visited.add(tuple(map(tuple, start)))
    
    # বাম, ডান, উপর, নিচ মুভমেন্টের জন্য
    row = [0, 0, -1, 1]
    col = [-1, 1, 0, 0]
    move_names = ["Left", "Right", "Up", "Down"] # বোঝার সুবিধার জন্য নাম দিলাম

    print("--- Simulation Start ---")

    while queue:
        # ২. কিউ থেকে সবার আগের বোর্ডটি বের করলাম
        current = queue.popleft()
        
        # ৩. চেক: এটা কি গোল?
        if is_goal(current.board):
            print(f"\n✅ Solution found at depth {current.depth}!")
            print("Final Board State:")
            for r in current.board: print(r)
            return

        # ৪. যদি গোল না হয়, নতুন মুভ ট্রাই করি
        for i in range(4):
            new_x = current.x + row[i]
            new_y = current.y + col[i]

            if is_valid(new_x, new_y):
                # নতুন বোর্ড তৈরি করা (Deep Copy)
                new_board = [r[:] for r in current.board]
                
                # 0 এবং পাশের সংখ্যার জায়গা বদল (Swap)
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                new_board[new_x][new_y], new_board[current.x][current.y]
                
                # ৫. নতুন বোর্ডটি যদি আগে না দেখে থাকি, তবে কিউ-তে যোগ করি
                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    queue.append(p8_board(new_board, new_x, new_y, current.depth + 1))
                    
    print("No solution found")

# --- Example Run ---
# ইনপুট বোর্ড
start_board = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 0, 8]
]
# এখানে 0 আছে (Row 2, Col 1) পজিশনে
bfs(start_board, 2, 1)