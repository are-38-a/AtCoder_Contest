#https://atcoder.jp/contests/abc207/tasks/abc207_c

n = int(input())
kukan = []

for num in range(n):
  t, l, r = map(int, input().split())
  if t == 2:
    r -= 0.01
  if t == 3:
    l += 0.01
  if t == 4:
    l += 0.01
    r -= 0.01
  kukan.append([l, r])

counter = 0
for i in range(n-1):
  for j in range(i+1,n):
    fukumu = False
    if kukan[j][0] <= kukan[i][1] and kukan[i][1]<=kukan[j][1]:
      fukumu = True
    elif kukan[i][0] <= kukan[j][1] and kukan[j][0] <= kukan[i][0]:
      fukumu = True
    elif kukan[i][0] <= kukan[j][0] and kukan[j][1] <= kukan[i][1]:
      fukumu = True
    if fukumu == True:
      counter += 1
print(counter)