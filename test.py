import random

# 1〜100のランダムな数を決める
answer = random.randint(1, 100)
tries = 0

print("=== 数当てゲーム ===")
print("1〜100の数を当ててください！")

while True:
    # プレイヤーの入力を受け取る
    guess = int(input("あなたの答え: "))
    tries += 1

    if guess < answer:
        print("もっと大きい数です！")
    elif guess > answer:
        print("もっと小さい数です！")
    else:
        print(f"正解！ 答えは {answer} でした！")
        print(f"試行回数: {tries} 回")
        break
