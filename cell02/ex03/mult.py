print("Enter the first number:")
first_number = int(input())

print("Enter the second number:")
second_number = int(input())
multiply = first_number * second_number

print(f"{first_number} x {second_number} = {multiply}")

if multiply > 0 :
    print("The result is positive.")

elif multiply < 0 :
    print("The result is negative.")

elif multiply == 0 :
    print("The result is positive and negative.")
