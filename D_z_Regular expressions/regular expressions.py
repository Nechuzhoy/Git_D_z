import re
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import io
from collections import OrderedDict
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


pattern = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[-\s]+(\d+)[-\s]+(\d+)\s*\(?(доб.)?\s*(\d{4})?"
pattern_2 = r"([А-Я]\w+)([,])?\s*([А-Я]\w+)([,\s])([А-Я]\w+)?([,])?([,])?([,])?"

replace = r" +7(\2)\3-\4-\5 \6\7"
replace_2 = r"\1 \3 \5\6"
replace_3 = r"\1,\3,\5\6\7\8,"

with open("phonebook1.csv", "w", encoding='utf-8') as f:
    for i , j in enumerate(contacts_list):
        result = re.sub(pattern, replace, ','.join(contacts_list[i]))
        result_2 = re.sub(pattern_2, replace_2, result)
        result_3  = re.sub(pattern_2, replace_3, result_2)
        s = io.StringIO(result_3)
        f.write(result_3)
        f.write('\n')

def remove_duplicates(list_: list) -> list:
    k = 0
    while k < len(list_) - 1:
        for list1, list2 in zip(list_[k], list_[k + 1]):
            if list1 == list2:
                new_list = list(OrderedDict.fromkeys(list_[k] + list_[k + 1]))
                list_.remove(list_[k + 1])
                list_.remove(list_[k])
                list_.append(new_list)
            break
        k += 1
    return list_
with open("phonebook1.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list_11 = list(rows)
    contacts_list_11 = sorted(contacts_list_11[1:])

contacts_list_1 = remove_duplicates(contacts_list_11 )

with open("phonebook1.csv", "w", encoding='utf-8') as f:
    for i , j in enumerate(contacts_list_1):
        s = io.StringIO(','.join(contacts_list_1[i]))
        f.write(','.join(contacts_list_1[i]))
        f.write('\n')


