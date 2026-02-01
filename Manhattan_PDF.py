from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Lab Report: Manhattan Distance Implementation', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_lab_report():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Content
    body_text = """Course Title: Artificial Intelligence
Lab Experiment: Heuristic Function Implementation for 8-Puzzle

1. Objective
------------------------------------------------------------
The main objective is to implement and calculate the Manhattan Distance for the 8-Puzzle problem using Python. We compare two methods:
1. Using a 1D List (Flat array).
2. Using a 2D Grid (Matrix).

2. Theory
------------------------------------------------------------
Manhattan Distance estimates how far the current state is from the goal. It calculates the total moves required for each tile to reach its correct position.

Formula: Distance = |Current_Row - Goal_Row| + |Current_Col - Goal_Col|

3. Implementation
------------------------------------------------------------

Method 1: Using 1D List (Code 01)
We use integer division (//) and modulus (%) to find row and column from a flat list index.

[Source Code 1]:
def manhattan_distance(state, goal):
    total_distance = 0
    for tile in range(1, 9):
        current_index = state.index(tile)
        goal_index = goal.index(tile)
        
        current_row = current_index // 3
        current_col = current_index % 3
        goal_row = goal_index // 3
        goal_col = goal_index % 3
        
        distance = abs(current_row - goal_row) + abs(current_col - goal_col)
        total_distance += distance
    return total_distance

Method 2: Using 2D Grid (Code 02)
We use a nested list (Matrix) and a helper function to find positions (row, col).

[Source Code 2]:
def find_position(grid, tile):
    for r in range(3):
        for c in range(3):
            if grid[r][c] == tile:
                return (r, c)
    return None

def manhattan_distance_2d(current, goal):
    total_dist = 0
    for tile in range(1, 9):
        pos_curr = find_position(current, tile)
        pos_goal = find_position(goal, tile)
        
        dist = abs(pos_curr[0] - pos_goal[0]) + abs(pos_curr[1] - pos_goal[1])
        total_dist += dist
    return total_dist

4. Result and Output
------------------------------------------------------------
Both methods produce the same heuristic value for the given input.
Output: Heuristic value: 14

5. Discussion & Comparison
------------------------------------------------------------
- Code 01 (1D): Faster and memory efficient. Uses math to find positions. Harder to visualize mentally.
- Code 02 (2D): Easier to read and understand (intuitive). Slightly slower due to loop-based searching.

6. Conclusion
------------------------------------------------------------
Both methods are correct. The 1D approach is better for performance, while the 2D approach is better for readability and understanding the grid structure.
"""
    
    # Write text to PDF
    pdf.multi_cell(0, 10, body_text)
    
    # Save the file
    file_name = "Lab_Report_Manhattan_Distance.pdf"
    pdf.output(file_name)
    print(f"Success! PDF generated as '{file_name}'")

if __name__ == "__main__":
    create_lab_report()