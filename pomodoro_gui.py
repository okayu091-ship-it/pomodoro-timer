import tkinter as tk
import datetime

WORK_MINUTES = 1
BREAK_MINUTES = 5
GRID_COLS = 8

root = tk.Tk()
root.title("ポモドーロタイマー")
root.geometry("500x600")
root.configure(bg="#2C2C2C")

# 状態管理
is_running = False
is_work_mode = True
completed_pomodoros = 0
remaining_seconds = WORK_MINUTES * 60
timer_id = None

title_label = tk.Label(root, text="ポモドーロタイマー", font=("Arial", 20, "bold"), bg="#2C2C2C", fg="white")
title_label.pack(pady=20)

mode_label = tk.Label(root, text="勉強中", font=("Arial", 16), bg="#2C2C2C", fg="#FF6B6B")
mode_label.pack()

timer_label = tk.Label(root, text="25:00", font=("Arial", 60, "bold"), bg="#2C2C2C", fg="white")
timer_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="#2C2C2C")
btn_frame.pack(pady=20)

start_btn = tk.Button(btn_frame, text="スタート", font=("Arial", 14), width=8, bg="#FF6B6B", fg="white", relief="flat")
start_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(btn_frame, text="リセット", font=("Arial", 14), width=8, bg="#555555", fg="white", relief="flat")
reset_btn.grid(row=0, column=1, padx=10)

total_label = tk.Label(root, text="累計: 0時間0分（0ポモドーロ）", font=("Arial", 12), bg="#2C2C2C", fg="#AAAAAA")
total_label.pack()

grid_frame = tk.Frame(root, bg="#2C2C2C")
grid_frame.pack(pady=20)

blocks = []
for i in range(40):
    block = tk.Label(grid_frame, text="  ", width=3, height=1, bg="#444444", relief="flat")
    row = i // GRID_COLS
    col = i % GRID_COLS
    block.grid(row=row, column=col, padx=3, pady=3)
    blocks.append(block)


def save_record():
    today = datetime.date.today()
    total_minutes = completed_pomodoros * WORK_MINUTES
    with open("study_record.txt", "a", encoding="utf-8") as f:
        f.write(f"{today} : {total_minutes}分（{completed_pomodoros}ポモドーロ）\n")



def update_display():
    mins, secs = divmod(remaining_seconds, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    total_minutes = completed_pomodoros * WORK_MINUTES
    hours = total_minutes // 60
    minutes = total_minutes % 60
    total_label.config(text=f"累計: {hours}時間{minutes}分（{completed_pomodoros}ポモドーロ）")


def update_blocks():
    for i, block in enumerate(blocks):
        if i < completed_pomodoros:
            block.config(bg="#FF6B6B")
        else:
            block.config(bg="#444444")


def switch_mode():
    global is_work_mode, remaining_seconds
    if is_work_mode:
        is_work_mode = False
        remaining_seconds = BREAK_MINUTES * 60
        mode_label.config(text="休憩中", fg="#6BCB77")
        timer_label.config(fg="#6BCB77")
    else:
        is_work_mode = True
        remaining_seconds = WORK_MINUTES * 60
        mode_label.config(text="勉強中", fg="#FF6B6B")
        timer_label.config(fg="white")
    update_display()


def tick():
    global remaining_seconds, is_running, completed_pomodoros, timer_id
    if remaining_seconds > 0:
        remaining_seconds -= 1
        update_display()
        timer_id = root.after(1000, tick)
    else:
        # タイマー終了
        if is_work_mode:
            completed_pomodoros += 1
            update_blocks()
            root.bell()  # 通知音
        else:
            save_record()

        switch_mode()
        is_running = False
        start_btn.config(text="スタート")


def toggle_start():
    global is_running, timer_id
    if is_running:
        is_running = False
        if timer_id:
            root.after_cancel(timer_id)
        start_btn.config(text="スタート")
    else:
        is_running = True
        start_btn.config(text="一時停止")
        tick()


def reset():
    global is_running, is_work_mode, remaining_seconds, timer_id
    if timer_id:
        root.after_cancel(timer_id)
    is_running = False
    is_work_mode = True
    remaining_seconds = WORK_MINUTES * 60
    mode_label.config(text="勉強中", fg="#FF6B6B")
    timer_label.config(fg="white")
    start_btn.config(text="スタート")
    update_display()


start_btn.config(command=toggle_start)
reset_btn.config(command=reset)

update_display()
root.mainloop()
