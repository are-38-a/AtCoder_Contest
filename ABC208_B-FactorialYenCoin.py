#https://atcoder.jp/contests/abc208/tasks/abc208_b

import math

p = int(input())
maisuu = 0
kouka_dict = {}

for n in range(10):
  kouka_dict[n+1] = 100

#最大の価格の硬貨を使用できるだけ使用する
for n in reversed(range(1,11)):
  while math.factorial(n) <= p:
    if kouka_dict[n] > 0:
      p -= math.factorial(n)
      maisuu += 1
    else:
      break
print(maisuu)