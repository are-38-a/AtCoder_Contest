# https://atcoder.jp/contests/abc204/tasks/abc204_b

N = int(input())
List = list(map(int, input().split()))

counter = 0
for n in List:
  if n > 10:
    counter += n - 10
print(counter)