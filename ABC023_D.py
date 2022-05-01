import io
import sys

_INPUT = """\
6
4
5 6
12 4
14 7
21 2
6
100 1
100 1
100 1
100 1
100 1
1 30
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  F=[list(map(int,input().split())) for _ in range(N)]
  l,r=0,10**15
  while r-l>1:
    mid=(l+r)//2
    tmp=[(mid-F[i][0])//F[i][1] for i in range(N)]
    tmp.sort()
    flg=0
    for i in range(N):
      if tmp[i]<i: flg=1
    if flg==0: r=mid
    else: l=mid
  print(r)