import time
import os

WORK_MINUTES = 25
BREAK_MINUTES = 5
GRID_COLS = 8  # 横に並ぶブロック数

completed_pomodoros = 0


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def show_progress():
    print("=== 累計学習時間 ===")
    total_minutes = completed_pomodoros * WORK_MINUTES
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(f"合計: {hours}時間{minutes}分 （{completed_pomodoros}ポモドーロ）")
    print()

    # ブロックで可視化（1ブロック＝25分）
    for i in range(max(completed_pomodoros, 1)):
        if i < completed_pomodoros:
            print("■", end=" ")
        else:
            print("□", end=" ")
        if (i + 1) % GRID_COLS == 0:
            print()
    print("\n")


def countdown(label, minutes):
    total_seconds = minutes * 60
    for remaining in range(total_seconds, 0, -1):
        clear()
        show_progress()
        mins, secs = divmod(remaining, 60)
        print(f"【{label}】")
        print(f"残り時間: {mins:02d}:{secs:02d}")
        time.sleep(1)


def main():
    global completed_pomodoros
    clear()
    print("=== ポモドーロタイマー ===")
    print(f"勉強: {WORK_MINUTES}分 → 休憩: {BREAK_MINUTES}分 を繰り返します")
    print("Ctrl+C で終了\n")
    input("準備ができたらEnterキーを押してください...")

    try:
        while True:
            # 勉強タイム
            countdown("勉強中", WORK_MINUTES)
            completed_pomodoros += 1

            clear()
            show_progress()
            print("お疲れ様！休憩しましょう")
            input("Enterキーを押すと休憩タイマーが始まります...")

            # 休憩タイム
            countdown("休憩中", BREAK_MINUTES)

            clear()
            show_progress()
            print("休憩終わり！次のポモドーロを始めましょう")
            input("Enterキーを押すと勉強タイマーが始まります...")

    except KeyboardInterrupt:
        clear()
        show_progress()
        print("お疲れ様でした！")


main()
