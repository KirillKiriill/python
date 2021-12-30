my_int = 8
my_float = 7.14
my_str = "Hi Kir"
my_list = ['g', '10']
my_tuple = ('h', '1')
my_dict = {'name': 'Kirill', 'sername': 'Sukhanov'}

my_document = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in my_document:
    print(f'{i} is {type(i)}')


element_count = int(input("Введите количество элементов списка "))
my_list = [1]
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)



seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])

my_string = input("введите предложение ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1





my_list = [5, 4, 3, 2, 1]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (000 - выход) "))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (000 - выход) "))