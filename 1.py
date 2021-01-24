import sys

digit_string = sys.argv[1]

summary = 0
digit_string = str(digit_string)

for digit in digit_string:
    summary += int(digit)

print(summary)
