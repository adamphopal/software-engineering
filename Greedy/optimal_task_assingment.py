# YouTube Video: https://www.youtube.com/watch?v=QvSIAB27Vdk
#Greedy Algorithms in Python: Optimal Task Assignment

#Assign tasks to workers such that the time it takes to complete all tasks is minimized.


A = [6, 3, 2, 7, 5, 5]

A = sorted(A)
print(A) #235567 take the min and pair it with the max in the sorted list, and create 3 workers
#2+7 = 9, 3+6=9, 5+5=10,= max= 10 = max amount of time all the workers will take is 10

for i in range(len(A)//2):
    print(A[i], A[~i])

#output will produce 3 pairs: from the sorted list [2, 3, 5, 5, 6, 7]
#1. (2 7)
#2. (3 6)
#3. (5 5)
