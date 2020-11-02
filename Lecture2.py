# WHILE ----> Tsikl beskonechnyi
# while условие:
#     тело цикла

# 1)

# count = 5
# while count <= 10:
#     print(count)
#     count += 1
# print('OK')

# 2)
# names = ['Atabek', 'Amanali', 'Alina']
# while len(names) > 2:                       -------->   chitaet skolko elementov
#     print(names.pop().title())

# 3)
# while True:
#     name = input('Введите ваше имя: ')
#     print(f'Hello, {name}')
#     q = input(" Для выхода введите 'q': ")
#     if q.lower()== 'q':
#         break ------> ostanavitsya, konets operatsiya

# 4)
# flag = True
# while flag:
#         name = input('Введите ваше имя: ')
#         print(f'Hello, {name}')
#         flag = input(" Для выхода введите 'Tab': ")

# Continue  ------>  
# for ----> 

#  5)
# for peremena in obekt:
#     telo sikla
# names = ['Atabek', 'Amanali', 'Alina']
# for x in names:
    # print(x.title())

# 6)
# some_string = 'python'
# count = 1
# for i in some_string:
#     print(f'Its {count} iteratsiya')
#     print(i)
#     count += 1

# 7)
# nums = [1,2,-3,4,5,-6,7,8,9,10,0]
# for num in nums:
#     if num > 0:
#         print(f'{num} - polojitelnoe')
#     elif num < 0:
#         print(f' {num} - otritsatelnoe')
#     else:
#         continue                              #------> perehodit k sleduishimi elementu
#     print(num)

# 8)
# nums = [1,2,-3,0,5,6,7,8,5,4]
# new_list = []
# for item in nums:
#     if item > 0:
#         new_list.append(item)
#     else:
#         continue
#     print(item)

# 9)

                       # RANGE ---> Fuksiya, diapazon 
                      # range(start, end, step)

# list_ = list(range(1, 10, 2))
# print(list_)

# 10)
# for x in range(1, 11):
#     print(x)

# 11)
# some_string = ['b', 'o', 'n', 'o', 'n', 'o']
# for x some_string:
# for x in range(len(some_string)):   #[0,1,2,3,4,5]  -----> skolko bukva est
    # print(some_string[x])  #    ------> po indexu naidet
#     if some_string[x] == 'o':
#         some_string[x] = 'a'
# print(''.join(some_string))       -----> koshulup zhazat, kogda izmenyeem

# 12)
# name = 'Gulzana'
# print(len(name))
# range(1, len(name), 2)
# range(7)
# [1, 3, 5]

# 13)
# name = 'Gulzana'
# x = 3
# new = name[x]





















