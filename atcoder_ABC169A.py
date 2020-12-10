# 169A

# 1.入力をちゃんと受け取ること
# ex: 「2 5」　=> a=2,b=5みたいにしないといけない
a, b = map(int, input().split())
# print(a)
# print(b)

# 2. 目的通りの計算をする
# ex: ２つの整数AとBの掛け算をやる
answer = a * b

# 3. 計算の結果を出力する
print(answer)