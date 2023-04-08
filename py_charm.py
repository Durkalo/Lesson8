def square(number):
    result = number ** 2
    return result
num = int(input("Insert your number: "))
squared_num = square(num)
print(f"Square of {num} = {squared_num}.")
