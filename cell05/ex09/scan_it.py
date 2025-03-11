import sys
sys.argv = ["scan_it.py", "apple", "apple banana apple"]
if len(sys.argv) != 3 :
    print("none")


keyword = sys.argv[1]
string = sys.argv[2]
count = string.count(keyword)

if count == 0 :
    print("none")
else :
    print(count)