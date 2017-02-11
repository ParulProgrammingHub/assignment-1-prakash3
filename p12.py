12)	 Write a python program that accepts an integer (n) and computes the value of n+nn+nnn.
Solution:
n=int(input("Enter number of your choice :"))
s=0
i=1
while (i<=3) :
       s=s+(n**i)
       i=i+1
print(s)
