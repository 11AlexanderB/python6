# task1.

# list =['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5','градусов']

# def search_sign(x):
#     """Функция для поиска чисел с знаками, принимает элемент из списка,
#     возвращает знак перед числом.
#     """
#     if x[0] in '+-':
#         return x[0]

# i = 0

# while i < len(list):
#     sign = search_sign(list[i])
#     if list[i].isdigit() or list[i][1:].isdigit():
#         if sign:
#             list[i]= sign + list[i][1:].zfill(2)
#         else:
#             list[i] = list[i].zfill(2)

#         list.insert(i, '"')
#         list.insert(i+2, '"')
#         i +=2
#     i +=1

# print(" ".join(list))


# task2

# list = ['инженер-конструктор Игорь','главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй','директор аэлита']
# for i in list:
#     i = i.split()[-1].title()
#     print(f'Привет, {i}!')

# task3 

# from random import uniform

# list_price = [round(uniform(1,20),2) for i in range(10)]

# def sort_ascending(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-i - 1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list

# def sort_descending(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-i - 1):
#             if list[j] < list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list

# def line_price(list):
#     for i in  range(len(list)):
#         list[i] = str(list[i]).split('.')
#         list[i] = str(list[i][0]).rjust(2, '0') + ' рублей ' + str(list[i][1]).ljust(2, '0') + ' копеек '
        
#     return list

# print(line_price(list_price))
# print(sort_ascending(list_price))
# print(sort_descending(list_price))
