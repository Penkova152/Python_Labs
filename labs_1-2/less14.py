
import random


def get_upper(string_list):
    return str(string_list[random.randint(0, len(string_list)-1)]).upper()


my_strings = ['строка1', 'строка2', 'строка3']

print(get_upper(my_strings))
