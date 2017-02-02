"""
Iterating multiple lists at the same time
"""

List1 = [1, 2, 3]
List2 = [6, 7, 8, 10, 20, 30]

for a, b in zip(List1, List2):
    if a > b:
        print(a)
    else:
        print(b)