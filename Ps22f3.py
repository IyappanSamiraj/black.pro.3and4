n=int(input())
num=list(map(int,input().split()))
m=sorted(num)
sum=m[-1]+m[-2]
print(sum)
