import random
a = random.randint(100000, 999999)
b = random.randint(100000, 999999)
c = random.randint(100000, 999999)
print(a, b, c)
count1 = 0
count2 = 0
for i in str(a):
    if(i == "1"):
        count1 += 1
    elif(i =="2"):
        count2 += 1
for i in str(b):
    if(i == "1"):
        count1 += 1
    elif(i =="2"):
        count2 += 1
for i in str(c):
    if(i == "1"):
        count1 += 1
    elif(i =="2"):
        count2 += 1
print(count2, "двоек", count1, "единиц")