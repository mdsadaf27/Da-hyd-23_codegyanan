# Task: Print A to Z using loops

# range(65, 91) generates numbers from 65 to 90
# 65 is the ASCII value of 'A'
# 90 is the ASCII value of 'Z'
# 91 is not included in range()

for i in range(65, 91):
    # chr() converts the ASCII value into a character
    print(chr(i), end=" ")




#task 2
# Observe +ve,+ve, -ve,-ve & +ve,-ve all possibilities

word = "Supercalifragilisticexpialidocious"

print(word)
print(len(word))

print(word[:])
print(word[5:])
print(word[:10])

print(word[-8:])
print(word[:-6])

print(word[4:-8])
print(word[-1:5])
print(word[6::-2])
