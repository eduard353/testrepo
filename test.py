import sys

digit_string = sys.argv[1]

digit_string = int(digit_string)

for x in range(1, digit_string+1):
    print(" "*(digit_string-x) + "#"*x)