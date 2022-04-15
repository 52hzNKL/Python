n = input()
characters = ""
number = ""
for i in n:
    if(i.isalpha()):
        characters += i
    else:
        number += i
newNumber = []
for i in number:
    newNumber.append(int(i))
for i in range (0, len(newNumber)):
    for j in range (0, len(newNumber)):
        if(newNumber[i] > newNumber[j]):
            a = newNumber[i]
            newNumber[i] = newNumber[j]
            newNumber[j] = a
newNumber = "".join([str(char) for char in newNumber])
print(characters)
print(newNumber)

