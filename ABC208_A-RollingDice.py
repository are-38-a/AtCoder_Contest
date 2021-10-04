#https://atcoder.jp/contests/abc208/tasks/abc208_a

a, b = map(int, input().split())
b2 = b

for i in range(a):
  b -= 6
if b <= 0 and b2 >= a:
  print("Yes")
else:
  print("No")