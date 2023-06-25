#Дан список повторяющихся элементов. 
#Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.


import collections
from collections import Counter

my_list = [1, 2, 3, 4, 12, 6, 6, 1, 12, 14, 2, 4]
test_list1 = set([x for x in my_list if my_list.count(x) > 1])
test_list2 = [x for x,k in Counter(my_list).items() if k > 1]
print(my_list)
print(list(test_list1))
print(test_list2)