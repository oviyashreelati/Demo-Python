import tkinter as tk
import random
import copy
import time
# --------------------sodoku generator--------------------
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums: 
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_puzzle(difficulty='medium'):
    board = [[0] * 9 for _ in range(9)]
    solve(board)
    puzzle = copy.deepcopy(board)
    # remove numbers based on difficulty
    if difficulty == 'easy':
        cells_to_remove = 30
    elif difficulty == 'medium':
        cells_to_remove = 40
    else:  # hard
        cells_to_remove = 50
    
    removed = 0
    while removed < cells_to_remove:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if puzzle[r][c] != 0:
            puzzle[r][c] = 0
            removed += 1
    return puzzle, board

#--------------------GUI--------------------
class Sodoku:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.difficulty = 'medium'
        self.start_time = time.time()
        self.timer_running = True
        
        # Info frame for difficulty and timer
        self.info_frame = tk.Frame(root)
        self.info_frame.pack(pady=5)
        
        self.difficulty_label = tk.Label(self.info_frame, text=f"Difficulty: {self.difficulty.upper()}",
                                         font=('Arial', 12, 'bold'))
        self.difficulty_label.grid(row=0, column=0, padx=20)
        
        self.timer_label = tk.Label(self.info_frame, text="Time: 00:00", font=('Arial', 12, 'bold'))
        self.timer_label.grid(row=0, column=1, padx=20)
        
        self.cells = [[None] * 9 for _ in range(9)]
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.puzzle, self.solution = generate_puzzle(self.difficulty)
        self.create_grid()
        self.create_buttons()
        self.update_timer()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                # Add thicker borders for 3x3 boxes
                padx_left = 5 if j % 3 == 0 else 1
                padx_right = 5 if (j + 1) % 3 == 0 else 1
                pady_top = 5 if i % 3 == 0 else 1
                pady_bottom = 5 if (i + 1) % 3 == 0 else 1
                
                entry = tk.Entry(self.frame, width=2, font=('Arial', 18), justify='center',
                               relief='solid', borderwidth=2)
                entry.grid(row=i, column=j,
                          padx=(padx_left, padx_right),
                          pady=(pady_top, pady_bottom))
                
                if self.puzzle[i][j] != 0:
                    entry.insert(0, str(self.puzzle[i][j]))
                    entry.config(state='disabled', disabledforeground='black',
                               disabledbackground='lightgray')
                self.cells[i][j] = entry

    def create_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Check", command=self.check,
                 font=('Arial', 10), width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="New Game", command=self.new_game,
                 font=('Arial', 10), width=10).grid(row=0, column=1, padx=5)
        
        # Difficulty selector
        tk.Label(btn_frame, text="Difficulty:", font=('Arial', 10)).grid(row=0, column=2, padx=5)
        self.difficulty_var = tk.StringVar(value='medium')
        difficulties = ['easy', 'medium', 'hard']
        for idx, diff in enumerate(difficulties):
            tk.Radiobutton(btn_frame, text=diff.capitalize(), variable=self.difficulty_var,
                          value=diff, font=('Arial', 9)).grid(row=0, column=3+idx, padx=2)
        
        self.result = tk.Label(self.root, text="", font=('Arial', 12, 'bold'))
        self.result.pack()
    
    def update_timer(self):
        if self.timer_running:
            elapsed = int(time.time() - self.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)

    def check(self):
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                if val == "" or int(val) != self.solution[i][j]:
                    self.result.config(text="Incorrect! Try again.", fg="red")
                    return
        
        # Stop timer on win
        self.timer_running = False
        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        self.result.config(text=f"Correct! You win! Time: {minutes:02d}:{seconds:02d}", fg="green")

    def new_game(self):
        # Get selected difficulty
        self.difficulty = self.difficulty_var.get()
        self.difficulty_label.config(text=f"Difficulty: {self.difficulty.upper()}")
        
        # Reset timer
        self.start_time = time.time()
        self.timer_running = True
        
        # Recreate grid
        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.puzzle, self.solution = generate_puzzle(self.difficulty)
        self.cells = [[None] * 9 for _ in range(9)]
        self.create_grid()
        self.result.config(text="")

#--------------------run---------------------
root = tk.Tk()
game = Sodoku(root)
root.mainloop()