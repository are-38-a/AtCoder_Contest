#https://atcoder.jp/contests/abc207/tasks/abc207_b

a, b, c, d = map(float, input().split())

mizuiro = a
aka = 0

#操作
sousakaisuu = 0
if b < c*d:
  while mizuiro > d*aka:
    mizuiro += b
    aka += c
    sousakaisuu += 1
else:
  sousakaisuu = -1
  
print(sousakaisuu)