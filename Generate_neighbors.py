import copy  # ফটোকপি করার মেশিন

def find_zero(grid):
    # পুরো গ্রিড খুঁজে ০ এর ঠিকানা বের করা
    for r in range(3):
        for c in range(3):
            if grid[r][c] == 0:
                return r, c
    return None

def generate_neighbors(current_state):
    neighbors = [] # এখানে সব নতুন বাচ্চাকাচ্চা (new states) জমা রাখব
    
    # ১. ০ কোথায় আছে খুঁজে বের করি
    zero_row, zero_col = find_zero(current_state)
    
    # ৪টা দিক: (row এর পরিবর্তন, col এর পরিবর্তন, দিকের নাম)
    # Up: row ১ কমে (-1), col ঠিক থাকে (0)
    moves = [
        (-1, 0, "UP"),   
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]
    
    for dr, dc, move_name in moves:
        new_row = zero_row + dr
        new_col = zero_col + dc
        
        # ২. বাউন্ডারি চেক: নতুন পজিশন কি বোর্ডের ভেতরে আছে?
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            
            # ৩. অদলবদল করার আগে বোর্ডের একটা ফটোকপি করি (Deep Copy)
            # এটা না করলে অরিজিনাল বোর্ড নষ্ট হয়ে যাবে!
            new_state = copy.deepcopy(current_state)
            
            # ৪. Swap (অদলবদল) করি
            # ০ এর জায়গায় পাশের জন, পাশের জনের জায়গায় ০
            val_to_swap = new_state[new_row][new_col]
            
            new_state[zero_row][zero_col] = val_to_swap # ০ এর জায়গায় ভ্যালু বসালাম
            new_state[new_row][new_col] = 0             # ভ্যালুর জায়গায় ০ বসালাম
            
            # ৫. নতুন স্টেটটা লিস্টে যোগ করি
            neighbors.append((new_state, move_name))
            
    return neighbors

# --- টেস্ট করি আমাদের উদাহরণ দিয়ে ---

current_state = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

print("বর্তমান অবস্থা:")
for row in current_state:
    print(row)
print("-------------------")

# ফাংশন কল
next_moves = generate_neighbors(current_state)

print(f"মোট {len(next_moves)} টি রাস্তায় যাওয়া যাবে:\n")

for state, name in next_moves:
    print(f"Move: {name}")
    for row in state:
        print(row)
    print("-------")