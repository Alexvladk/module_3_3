def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [4, False, 'str']
print_params(*values_list)
values_dict = {'a':3, 'b':True, 'c':'string_'}
print_params(**values_dict)

values_list_2 = [5,'строка_']
print_params(*values_list_2, 42)