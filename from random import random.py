from random import random
import random
names = ["mahya","ali","shadi","nazi","mahtab","mozhdeh"]
answer = random.choice(names)
list = []
wrong = []
for i in range(len(answer)):
    list.append('_')

print("  ".join(list))

user = input("your letter: ")

if answer.find(user) == -1:
    wrong.append(user) 

else:
    for i in range(len(answer)):
        if answer[i] == user:
            list[i] = user        
        else:
            continue

print(list)
#while True:
