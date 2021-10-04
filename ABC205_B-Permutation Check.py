#https://atcoder.jp/contests/abc205/tasks/abc205_b
N = int(input())
target_list = list(map(int, input().split()))

N_list = [n for n in range(1, N+1)]

target_list.sort()

if N_list == target_list:
  print("Yes")
else:
  print("No")
