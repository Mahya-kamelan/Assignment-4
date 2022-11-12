numbers_list = []
sort = True
sortnumber = int(input("how many numbers do you want to check? "))
for i in range(0, sortnumber):
    number = int(input('Enter a number: '))
    numbers_list.append(number)
for number in range(1, sortnumber):
    if numbers_list[number -1] < numbers_list[number] or numbers_list[-number] < numbers_list[-number - 1]:
        sort = True
    else:
        sort = False
        break
if sort == True:
    print('Yup, all sort')
else:
    print('Nop, not sort')