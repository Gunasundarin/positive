N=int(input())
reverse=0
while N > 0:
  rem = N % 10
  reverse = (reverse * 10) + rem
  N = N // 10
print(reverse)
