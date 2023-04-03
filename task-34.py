"""   Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться 
в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения
одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
*Пример:*
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
**Вывод:** Парам пам-пам  """

def count_syllables(word):
    vowels = 'aeiouy'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

verse = input('Введите стихотворение: ')
sentence = verse.split()
syllables_per_phrase = [count_syllables(phrase) for phrase in sentence]
if len(set(syllables_per_phrase)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')


# Объяснение кода:
# 1. Начинаем с определения функции `count_syllables`, которая получает слово в качестве аргумента и возвращает количество слогов в слове. Мы получаем число гласных букв и считаем их как слоги.
# 2. Запрашиваем у пользователя ввод стихотворения и использовать метод `split()` для разделения стихотворения на отдельные фразы.
# 3. Используем генератор списка `syllables_per_phrase` для создания списка, в котором для каждой фразы указано количество слогов в ней.
# 4. Если все значения в списке `syllables_per_phrase` одинаковые, то значит, что ритм соблюдается, и мы выводим сообщение "Парам пам-пам". Иначе, если есть хотя бы одно значение, отличное от других, то ритм не соблюдается и мы выводим сообщение "Пам парам".