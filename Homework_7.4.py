# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного
# виразу (range) для 100 елементів, за наступними правилами:
#
# Один список з числами кратними 3, інший з кратними числами 5.
#
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
#
# Функція повинна повернути цю множину як результат своєї роботи.

def common_elements():
    set_of_multiples_of_3 = {element_of_3 for element_of_3 in range(100) if element_of_3 % 3 == 0}
    set_of_multiples_of_5 = {element_of_5 for element_of_5 in range(100) if element_of_5 % 5 == 0}
    intersection_set = set_of_multiples_of_3 & set_of_multiples_of_5
    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
