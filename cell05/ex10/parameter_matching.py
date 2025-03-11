import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit()

expected_word = sys.argv[1]
user_input = input()
if user_input == expected_word:
    print("Good job")
else: 
    print("Nope, sorry...")