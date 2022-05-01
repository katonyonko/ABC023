import io
import sys

_INPUT = """\
6
3
abc
6
abcabc
7
atcoder
19
bcabcabcabcabcabcab
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  tmp=['b','a','c']
  if N%2==0: print(-1)
  else:
    ans=N//2
    for i in range(N):
      if S[i]!=tmp[(N//2-i)%3]: ans=-1
    print(ans)