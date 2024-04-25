cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for car in cars:
    print(f"Я езжу на автомобиле марки {car}")
    cars_count += 10
    print(f"Текущее количество машин:{cars_count}")



letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа' # строку состоящую из русских букв разных регистров, необходимо  очистить от заглавных литер. 
clean_string = ''
for letter in letters:
    if not letter.isupper():
        clean_string += letter
letters = clean_string
print(letters)





# list_ = ['one', 'two', 'three', 'four']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
#
# print(list_)
#
# list_ = ['one', 'two', 'three', 'four']
# for i in range(5):
#     print(i)
#
# print(list_)
#
# list_ = ['one', 'two', 'three', 'four']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)):
#    sum_ += list_2[i]
#
# print(sum_)
#
# for i in range(1, 11): # i - начала цикла от 1 до 10
#     for j in range(1, 11): # j - второй элемент цикла от 1 до 10
#         print(f'{i} x {j} = {i * j}') # цикл начинается с i и перебирает все значения второго элемента цикла
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}# функция фор for  так же работает со словорями
#
# for i, k  in dict_.items():# в for можно задать несколько переменных
#     print(i, k)# при выводе мы видим сразу два значения словоря
