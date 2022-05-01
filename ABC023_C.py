import io
import sys

_INPUT = """\
6
3 5 3
5
1 2
2 1
2 5
3 2
3 5
7 3 1
4
3 2
3 3
4 2
4 3
5 5 2
5
1 1
2 2
3 3
4 4
5 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  R,C,K=map(int,input().split())
  N=int(input())
  d1,d2=defaultdict(int), defaultdict(int)
  rc=[]
  for i in range(N):
    r,c=map(int,input().split())
    rc.append([r,c])
    d1[r]+=1; d2[c]+=1
  d3,d4=defaultdict(int), defaultdict(int)
  for r in d1: d3[d1[r]]+=1
  for c in d2: d4[d2[c]]+=1
  d3[0]=R-len(d1)
  d4[0]=C-len(d2)
  ans=0
  for k in d3:
    if K-k in d4: ans+=d3[k]*d4[K-k]
  for i in range(N):
    r,c=rc[i]
    if d1[r]+d2[c]==K: ans-=1
    if d1[r]+d2[c]==K+1: ans+=1
  print(ans)