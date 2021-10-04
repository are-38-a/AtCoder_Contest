#https://atcoder.jp/contests/abc210/tasks/abc210_a

n, a, x, y = map(int, input().split())
ans = 0
if n > a:
  ans = (n-a) * y + a * x
else:
  ans = n * x
print(ans)