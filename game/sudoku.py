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
        self.root.title("🎮 Sudoku Game")
        self.root.configure(bg='#2C3E50')  # Dark blue-gray background
        self.difficulty = 'medium'
        self.start_time = time.time()
        self.timer_running = True
        
        # Title
        title_label = tk.Label(root, text="SUDOKU", font=('Arial', 24, 'bold'),
                              bg='#2C3E50', fg='#ECF0F1')
        title_label.pack(pady=10)
        
        # Info frame for difficulty and timer
        self.info_frame = tk.Frame(root, bg='#34495E', relief='raised', bd=2)
        self.info_frame.pack(pady=10, padx=20, fill='x')
        
        self.difficulty_label = tk.Label(self.info_frame, text=f"Difficulty: {self.difficulty.upper()}",
                                         font=('Arial', 12, 'bold'), bg='#34495E', fg='#F39C12')
        self.difficulty_label.grid(row=0, column=0, padx=30, pady=8)
        
        self.timer_label = tk.Label(self.info_frame, text="⏱ Time: 00:00",
                                    font=('Arial', 12, 'bold'), bg='#34495E', fg='#3498DB')
        self.timer_label.grid(row=0, column=1, padx=30, pady=8)
        
        self.cells = [[None] * 9 for _ in range(9)]
        self.frame = tk.Frame(root, bg='#1A252F', relief='solid', bd=3)
        self.frame.pack(pady=10)
        self.puzzle, self.solution = generate_puzzle(self.difficulty)
        self.create_grid()
        self.create_buttons()
        self.update_timer()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                # Add thicker borders for 3x3 boxes
                padx_left = 6 if j % 3 == 0 else 1
                padx_right = 6 if (j + 1) % 3 == 0 else 1
                pady_top = 6 if i % 3 == 0 else 1
                pady_bottom = 6 if (i + 1) % 3 == 0 else 1
                
                # Alternating colors for 3x3 boxes
                box_row = i // 3
                box_col = j // 3
                is_dark_box = (box_row + box_col) % 2 == 0
                
                entry = tk.Entry(self.frame, width=2, font=('Arial', 20, 'bold'),
                               justify='center', relief='solid', borderwidth=1)
                entry.grid(row=i, column=j,
                          padx=(padx_left, padx_right),
                          pady=(pady_top, pady_bottom))
                
                if self.puzzle[i][j] != 0:
                    entry.insert(0, str(self.puzzle[i][j]))
                    # Pre-filled cells with distinct styling
                    bg_color = '#E8F4F8' if is_dark_box else '#FFF9E6'
                    entry.config(state='disabled', disabledforeground='#2C3E50',
                               disabledbackground=bg_color, font=('Arial', 20, 'bold'))
                else:
                    # Editable cells with white background
                    bg_color = '#FFFFFF' if is_dark_box else '#F8F9FA'
                    entry.config(bg=bg_color, fg='#16A085', insertbackground='#16A085',
                               font=('Arial', 20, 'bold'))
                
                self.cells[i][j] = entry

    def create_buttons(self):
        btn_frame = tk.Frame(self.root, bg='#2C3E50')
        btn_frame.pack(pady=15)
        
        # Check button with green theme
        check_btn = tk.Button(btn_frame, text="✓ Check Solution", command=self.check,
                             font=('Arial', 11, 'bold'), width=15,
                             bg='#27AE60', fg='white', activebackground='#229954',
                             relief='raised', bd=3, cursor='hand2')
        check_btn.grid(row=0, column=0, padx=8)
        
        # New game button with blue theme
        new_btn = tk.Button(btn_frame, text="🔄 New Game", command=self.new_game,
                           font=('Arial', 11, 'bold'), width=15,
                           bg='#3498DB', fg='white', activebackground='#2980B9',
                           relief='raised', bd=3, cursor='hand2')
        new_btn.grid(row=0, column=1, padx=8)
        
        # Difficulty selector frame
        diff_frame = tk.Frame(self.root, bg='#34495E', relief='raised', bd=2)
        diff_frame.pack(pady=10, padx=20)
        
        tk.Label(diff_frame, text="Select Difficulty:", font=('Arial', 11, 'bold'),
                bg='#34495E', fg='#ECF0F1').grid(row=0, column=0, padx=10, pady=8)
        
        self.difficulty_var = tk.StringVar(value='medium')
        difficulties = [('Easy', 'easy', '#27AE60'), ('Medium', 'medium', '#F39C12'), ('Hard', 'hard', '#E74C3C')]
        
        for idx, (label, value, color) in enumerate(difficulties):
            rb = tk.Radiobutton(diff_frame, text=label, variable=self.difficulty_var,
                               value=value, font=('Arial', 10, 'bold'),
                               bg='#34495E', fg=color, selectcolor='#2C3E50',
                               activebackground='#34495E', activeforeground=color,
                               cursor='hand2')
            rb.grid(row=0, column=1+idx, padx=8, pady=8)
        
        # Result label with better styling
        self.result = tk.Label(self.root, text="", font=('Arial', 14, 'bold'),
                              bg='#2C3E50', fg='white', pady=10)
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
                    self.result.config(text="❌ Incorrect! Keep trying...",
                                     fg="#E74C3C", bg='#2C3E50')
                    # Highlight incorrect cells briefly
                    self.root.after(2000, lambda: self.result.config(text=""))
                    return
        
        # Stop timer on win
        self.timer_running = False
        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        self.result.config(text=f"🎉 Congratulations! You solved it in {minutes:02d}:{seconds:02d}!",
                          fg="#27AE60", bg='#2C3E50')

    def new_game(self):
        # Get selected difficulty
        self.difficulty = self.difficulty_var.get()
        
        # Update difficulty label with color
        diff_colors = {'easy': '#27AE60', 'medium': '#F39C12', 'hard': '#E74C3C'}
        self.difficulty_label.config(text=f"Difficulty: {self.difficulty.upper()}",
                                    fg=diff_colors[self.difficulty])
        
        # Reset timer
        self.start_time = time.time()
        self.timer_running = True
        
        # Recreate grid
        self.frame.destroy()
        self.frame = tk.Frame(self.root, bg='#1A252F', relief='solid', bd=3)
        self.frame.pack(pady=10)
        self.puzzle, self.solution = generate_puzzle(self.difficulty)
        self.cells = [[None] * 9 for _ in range(9)]
        self.create_grid()
        self.result.config(text="")

#--------------------run---------------------
root = tk.Tk()
game = Sodoku(root)
root.mainloop()