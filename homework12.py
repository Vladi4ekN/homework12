##Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
   print(a, b, c)


print_params()

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



print_params(5, 'строка', True)
print_params(5, 'новая строка', True)
print_params(10, 'новая строка', False)
print_params()
print_params(b = 25) # выдаётся ошибка
print_params(c= [1, 2, 3]) # выдаётся ошибка

##Распаковка параметров:
def print_params (a, b, c):
    print(a, b, c)


values_list_ = [5, 'Vlad', True]
values_dict_ = {'a': 100, 'b': 'Dima', 'c': False}
print_params(*values_list_)
print_params(**values_dict_)

##Распаковка + отдельные параметры:
def print_params (a, b):
    print(a, b)


values_list_2 = [5, 'Vlad']
print_params(*values_list_2, 42) #выдаёт ошибку потому, что второй параметр не принимает никакого значения, в отличии от первого. Параметры должны принимать или оба значения, или второй

