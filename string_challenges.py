# Вывести последнюю букву в слове
word = 'Архангельск'
last = word[-1]
print(last)


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
list = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я']
count = 0
for letter in word:
    if letter in list:
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
a = sentence.split(' ')
for letters in a:
    first = letters[0]
    print(first)


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
a = sentence.split(' ')
length = len(a)
count = 0
for words in a:
    b = len(words)
    count += b
print(count/length)