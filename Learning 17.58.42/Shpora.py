
#Переменные и типы данных

boolean #- логическое значение True или False

int #- представляет целое число 7

float #- представляет число с плавающей точкой, например, 1.2 или 34.76

str #- строки, например "hello".

list #- список

    #Example

    numbers = [1, 2, 3, 4, 5]


range(end): создается набор чисел от 0 до числа end

range(start, end): создается набор чисел от числа start до числа end

range(start, end, step): создается набор чисел от числа start до числа end с шагом step


    #Example

    numbers = list(range(10))
    print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = list(range(2, 10))
    print(numbers)      # [2, 3, 4, 5, 6, 7, 8, 9]
    numbers = list(range(10, 2, -2))
    print(numbers)      # [10, 8, 6, 4]

tuple #- кортеж, кортеж является неизменяемым типом

    #Example

    user = ("Tom", 23)
    print(user)

dict #- словарь, где каждый элемент имеет ключ и значение

dictionary = { ключ1:значение1, ключ2:значение2, ....}

    #Example

    users = {1: "Tom", 2: "Bob", 3: "Bill"}

    user_id = 234
    print(type(user_id))  # <class 'int'> С помощью функции type() можно узнать текущий тип переменной


            #Арифметические операции

print(6 + 2)  # 8 Сложение двух чисел

print(6 - 2)  # 4 Вычитание двух чисел

print(6 * 2)  # 12 Умножение двух чисел

print(6 / 2)  # 3.0 Деление двух чисел

print(7 // 2)  # 3 Целочисленное деление двух чисел

print(6 ** 2)  # Возводим число 6 в степень 2. Результат - 36

print(7 % 2)  # Получение остатка от деления числа 7 на 2. Результат - 1

    #Example

    number = 10
    number += 5 #Присвоение результата сложения

    string = "hello world"
    length = len(string)
    print(length)   # 11 Для получения длины строки можно использовать функцию len()

         27/02/2018


     #Операции сравнения

==

Возвращает True, если оба операнда равны. Иначе возвращает False.

!=

Возвращает True, если оба операнда НЕ равны. Иначе возвращает False.

> (больше чем)

Возвращает True, если первый операнд больше второго.

< (меньше чем)

Возвращает True, если первый операнд меньше второго.

>= (больше или равно)

Возвращает True, если первый операнд больше или равен второму.

<= (меньше или равно)

    #Example

    a = 5
    b = 6
    result = 5 == 6  # сохраняем результат операции в переменную
    print(result)  # False - 5 не равно 6
    print(a != b)  # True
    print(a > b)  # False - 5 меньше 6
    print(a < b)  # True


            #Операции со строками

Для объединения строк применяется знак плюса +

    #Example

    name = "Jymy"
    surname = "Abrams"
    fullname = name + " " + surname
    print(fullname)  # Jymy Abrams

Если нам надо сложить строку и число, необходимо привести число к строке с помощью функции str()

    #Example

    name = "Jymy"
    age = 25
    info = "Name: " + name + " Age: " + str(age)
    print(info)  # Name: Jymy Age: 25


            # Оператор %

Оператор % после строки используется для объединения строки с переменными. Оператор % заменит %s в строке строковой переменной,
которая появится после нее.

    #Example

    string_1 = "Moscow"
    string_2 = "city"

    print ("Let's not go to %s. This a silly %s." % (string_1, string_2))
    # Let's not go to Moscow. 'Tis a silly city.

\n перенос строки

    #Example

    print("Это длинная строка\nнужно ее перенести")

    #Это длинная строка
    #нужно ее перенести

\t табуляция

    print("Это длинная строка\tнужно ее перенести")
    #Это длинная строка    нужно ее перенести

Функция lower() приводит строку к нижнему регистру, а функция upper() - к верхнему

    #Example

    str1 = "Jymy"
    str2 = "jymy"
    print(str1 == str2)  # False - строки не равны

    print(str1.lower() == str2.lower())  # True

            # Дата и время


    from datetime import datetime  # импортируем библиотеку

    now = datetime.now()
    print(now)  # 2018-02-08 10:22:26.613397
    print(now.year)  # 2018
    print(now.month)  # 2
    print(now.day)  # 8

    можно написать так

    from datetime import datetime  # импортируем библиотеку

    now = datetime.now()
    print('%s/%s/%s' % (now.month, now.day, now.year))  # 2/8/2018
    print('%s:%s:%s' % (now.hour, now.minute, now.second))  # 10:27:56

    можно все вместе

    print('%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second))
    # 2018/2/8 10:26:25
    мы можем менять: на - или : или / короче, как лучше для вас


        #Условная конструкция if

if логическое_выражение:
    инструкции
elif логическое выражение:
    инструкции
else:
    инструкции

    # Example

age = 18
if age > 21:
    print("Наслаждайся")
else:
    print("Подрости еще")

    # Цикл while

    while условное_выражение:
        инструкции

    i = 1000
    while i > 100:
        print(i)
        i /= 2   # 1000; 500.0; 250.0; 125.0


    # Цикл for

for int_var in функция_range:
    инструкции


for i in range(1, 5):
    print(i, end=" ") # 1 2 3 4

for i in range(1, 10):
    for g in range(1, 10):
        print(i * g, end="\t")
    print(i, end="\n")

   # Функция range

range(stop): возвращает все целые числа от 0 до stop

range(start, stop): возвращает все целые числа в промежутке от start (включая) до stop (не включая). Выше в программе факториала использована именно эта форма.

range(start, stop, step): возвращает целые числа в промежутке от start (включая) до stop (не включая), которые увеличиваются на значение step

range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4
range(2, 10, 2)     # 2, 4, 6, 8
range(5, 0, -1)     # 5, 4, 3, 2, 1
