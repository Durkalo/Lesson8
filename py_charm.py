def square(number):
    result = number ** 2
    return result
num = int(input("Insert your number: "))
squared_num = square(num)
print(f"Square of {num} = {squared_num}.")

def test_function(a,b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
test_function(7, 10)

