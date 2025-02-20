first = int(input("Enter The First number from where u want to Start the operation: "))
last = int(input("Enter The Second number to the spot u want to End the operation: "))

def square_numbers(first,last):
    x = []
    even_squares=[]
    odd_squares=[]
    
    for num in range(first,last+1):
        square = num*num
        x.append(square)
        
    for i in x:
        if i % 2 == 0:
            even_squares.append(i)
        else:
            odd_squares.append(i)
    
    print(f"Even Number Squares: {even_squares}\n")
    print(f"Odd Number Squares: {odd_squares}")
    
square_numbers(first,last)