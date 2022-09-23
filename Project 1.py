# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

stroka = 'абвгдейка - это передача'
words = stroka.split(' ')
fragment = 'абв'
new_words = []
for i in words:
    if fragment not in i:
        new_words.append(i)
_str = " ".join(new_words)
print(_str)

