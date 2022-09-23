# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

ls1 = ['python', 'c#', 'javascript', 'go']
def Cortej_List(input_list):
    input_list = list(map(str.upper, input_list))
    list2 = [i for i in range(1, len(input_list) + 1)]
    Cort_list = list(zip(list2, input_list))
    return Cort_list

def sum_symbol(input_list):
    input_list = list(map(str.upper, input_list))
    list2=[]
    list3 = [i for i in range(1, len(input_list) + 1)]
    word1 = 0
    for i in input_list[0]:
        word1 += (ord(i))
    word2 = 0
    for i in input_list[1]:
        word2 += (ord(i))
    word3 = 0
    for i in input_list[2]:
        word3 += (ord(i))
    word4 = 0
    for i in input_list[3]:
        word4 += (ord(i))
    if word1 % list3[0] == 0:
        list2.append(word1)
    if word2 % list3[1] == 0:
        list2.append(word2)
    if word3 % list3[2] == 0:
        list2.append(word3)
    if word4 % list3[3] == 0:
        list2.append(word4)
    Cort_list = list(zip(list2, input_list))
    print(f'Cумма слова ({input_list[0]}) в ASCII коде --> {word1}, Cумма слова ({input_list[1]}) в ASCII коде --> {word2}, Cумма слова ({input_list[2]}) в ASCII коде --> {word3}, Cумма слова ({input_list[3]}) в ASCII коде --> {word4}')
    return Cort_list


print(Cortej_List(ls1))
print(sum_symbol(ls1))








