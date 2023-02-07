import math

Values = input("Enter D: ")
Values = Values.split(',')

result = []
for D in Values:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result.append(Q)

print(result)
