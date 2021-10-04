"""
https://atcoder.jp/contests/abc204/tasks/abc204_a

問題文
サーバル、フェネック、アライグマの 3 人がじゃんけんをして、あいこになりました。

フェネックが出した手を表す文字 x とアライグマが出した手を表す文字 y が与えられます。それぞれ、0 はグー、1 はチョキを、2 はパーを表します。

サーバルが出した手を表す文字を出力してください。なお、答えは一意に定まります。"""

a,b = map(int,input().split())

if a == b:
  print(a)
else:
  if a == 0 and b ==1:
    print(2)
  if a == 1 and b == 2:
    print(0)
  if a == 2 and b == 0:
    print(1)
  if a == 0 and b == 2:
    print(1)
  if a == 1 and b == 0:
    print(2)
  if a ==2 and b == 1:
    print(0)