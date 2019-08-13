n=int(input())
num=list(map(int,input().split()))
m=sorted(num)
sum=m[-1]+m[-3]
if sum>=n:
	print(sum)
else:
	n=sum+m[-5]
	print(n)
