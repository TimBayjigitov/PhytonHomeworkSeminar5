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








