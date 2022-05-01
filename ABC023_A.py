import io
import sys

_INPUT = """\
6
23
70
99
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X=input()
  print(int(X[0])+int(X[1]))