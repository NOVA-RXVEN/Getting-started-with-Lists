l1 = [3,4,6,10,7,8,2,1,5]
print(f"The original list is: {l1}")

sum = 0

for i in l1:
    sum  = sum + i
    
print(f"The sum of numbers is: {sum}")

avg = sum/len(l1)
print(f"The average of the numbers in the list is : {avg}")

l1.sort()
print(f"The sorted list in ascending order: {l1}")

print(f"The largest element: {l1[-1]}")
print(f"The smallest element: {l1[0]}")
    