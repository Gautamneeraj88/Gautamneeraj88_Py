"""
6.Consider a tuple t1 = {1,2,5,7,9,2,4,6,8,10}.Write a program to perform following
operations:
a)Print another tuple whose values are even numbers in the given tuple.
b)Concatenate a tuple t2={11,13,15) with t1.
c)Return maximum and minimum value from this tuple.
"""
t1 = (1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
l1 = list()
length = len(t1)

for i in range(0, length, 1):
    
    if(t1[i] % 2 == 0):
        l1.append(t1[i])
t3 = tuple(l1)
print("Even number present in the given tuple: ",t3)

t4 = t1 + t2
print("Concatenated tuple is: ", t4)

print("Maximum number is: ",max(t4))
print("Minimum number is: ",min(t4))

maximum = t4[0]
minimum = t4[0]
for i in range(1, len(t4), 1):
    if (t4[i] > maximum):
        maximum = t4[i]
    if (t4[i] < minimum):
        minimum = t4[i]
print("Maximum :", max, "\tMinimum :", min)
