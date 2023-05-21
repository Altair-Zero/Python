
string = str(input("Введите строку: "))     # вводим строку
if string.count(',') != 0:                  # Удаляем знаки препинания
    string = string.replace(',', '')        
print(string)
words = string.split()

max_word = ''           # самое длинное слово
word_lenght = 0         # длинна самого слова
most_common_word = ''   # самое частое слово
count_most_common = 0   # количество самых частых слов
max_common_word = 0     # максимальное количество самых частых слов

for word in words:      # поиск самого длинного слова
    if word_lenght < len(word): 
        word_lenght = len(word)
        max_word = word

    for word_popular in words:   #Cколько раз в тексте встретилось слово
        if word == word_popular:
            count_most_common += 1

    if count_most_common > max_common_word:    # сравниваем с текущим максимальным количеством
        most_common_word = word                  
        max_common_word = count_most_common

    count_most_common = 0                     

print(f"Самое длинное слово: {max_word}.Его длинна =  {word_lenght}.")
print(f"Наиболее часто встречающееся слово: {most_common_word}.Всего таких слов: {max_common_word}.")