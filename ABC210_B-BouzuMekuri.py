#https://atcoder.jp/contests/abc210/tasks/abc210_b

n = int(input())
s = list(input())

pointer = 0

while s[pointer] != "1":
  pointer += 1

if pointer%2 == 1:
  print("Aoki")
else:
  print("Takahashi")