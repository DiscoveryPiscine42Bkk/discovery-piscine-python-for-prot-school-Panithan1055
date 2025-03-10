print("Enter a number less than 25 :")
numeric = int(input())
if numeric > 25 :
    print("Error")
elif numeric <= 25 :
    loop = 25 - numeric
    for i in range ((loop)+1) :
        print(f"Inside the loop, my variable is {numeric + i}")