import random
counter = 1
times_to_use = int(input("how many numbers do you want?"))
listt = []
if times_to_use <= 0 or times_to_use > 100:
    print("times to use must be between 1 and 99.")
else:
    for i in range(times_to_use):
        numbers = random.randint(0,99)
        if numbers in listt:
            counter -= 1
        else:
            listt.append(numbers)
        counter += 1
    print(listt)