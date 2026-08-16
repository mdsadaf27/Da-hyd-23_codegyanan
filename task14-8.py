"""

s = input("Enter a string: ")

for i in tuple(s):
    c = 0

    for j in tuple(s):
        if i == j:
            c = c + 1

    if c > 1:
        print(i, "is repeating", c, "times")
"""
#programming

s = input()

done = ()

for i in tuple(s):
    if i not in done:
        if s.count(i) > 1:
            print(i, "is repeating", s.count(i), "times")
        done += (i,)

