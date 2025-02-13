empty = []
print(empty)
print(type(empty))

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers)
print(numbers[0])
print(numbers[4])

numbers.append("Liban")
numbers.append("Sadab")
numbers.append("Nahian")
print(numbers)

numbers.pop()
numbers.pop()
numbers.pop()
print(numbers)

print()

triples = [1,2,3,4,5,6,7,8,9,10] * 5
print(triples)

aList = [100,200,300,400,500,600,700,800,900,1000]
print(aList[::-1])