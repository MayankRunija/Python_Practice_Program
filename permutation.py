#permutation
n=int(input("Enter a total items : "))
r=int(input("Enter the no of item to be arrange : "))
#calculate n factorial
fact_n=1
for i in range(1,n + 1):
    fact_n *=i
#calculate n-r factorial
x=n-r
fact_x=1
for i in range (1,x+1):
    fact_x*=1
p= fact_n /fact_x
print(p)

