import sys
if len(sys.argv) < 2 :
    print("none")
else:
    reverse = sys.argv[1:][::-1]
    for param in reverse :
        print(param)
 