import tkinter as tk

WORK_MINUTES = 25
BREAK_MINUTES = 5
GRID_COLS = 8

# メインウィンドウ
root = tk.Tk()
root.title("ポモドーロタイマー")
root.geometry("500x600")
root.configure(bg="#2C2C2C")

# タイトル
title_label = tk.Label(
    root,
    text="ポモドーロタイマー",
    font=("Arial", 20, "bold"),
    bg="#2C2C2C",
    fg="white"
)
title_label.pack(pady=20)

# モード表示（勉強中 / 休憩中）
mode_label = tk.Label(
    root,
    text="勉強中",
    font=("Arial", 16),
    bg="#2C2C2C",
    fg="#FF6B6B"
)
mode_label.pack()

# タイマー表示
timer_label = tk.Label(
    root,
    text="25:00",
    font=("Arial", 60, "bold"),
    bg="#2C2C2C",
    fg="white"
)
timer_label.pack(pady=10)

# ボタンフレーム
btn_frame = tk.Frame(root, bg="#2C2C2C")
btn_frame.pack(pady=20)

start_btn = tk.Button(
    btn_frame,
    text="スタート",
    font=("Arial", 14),
    width=8,
    bg="#FF6B6B",
    fg="white",
    relief="flat"
)
start_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(
    btn_frame,
    text="リセット",
    font=("Arial", 14),
    width=8,
    bg="#555555",
    fg="white",
    relief="flat"
)
reset_btn.grid(row=0, column=1, padx=10)

# 累計時間表示
total_label = tk.Label(
    root,
    text="累計: 0時間0分（0ポモドーロ）",
    font=("Arial", 12),
    bg="#2C2C2C",
    fg="#AAAAAA"
)
total_label.pack()

# 塗り絵ブロックエリア
grid_frame = tk.Frame(root, bg="#2C2C2C")
grid_frame.pack(pady=20)

blocks = []
for i in range(40):
    block = tk.Label(
        grid_frame,
        text="  ",
        width=3,
        height=1,
        bg="#444444",
        relief="flat"
    )
    row = i // GRID_COLS
    col = i % GRID_COLS
    block.grid(row=row, column=col, padx=3, pady=3)
    blocks.append(block)

root.mainloop()
