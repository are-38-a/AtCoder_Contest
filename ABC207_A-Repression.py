#https://atcoder.jp/contests/abc207/tasks/abc207_a
numlist = list(map(int, input().split()))
sumlist = []

for n in range(len(numlist)):
  for m in range(len(numlist)):
    if m != n:
      sumlist.append(numlist[m]+numlist[n])

print(max(sumlist))
