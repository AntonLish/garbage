'''
6.1
a = 'Чехов'
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
b = " - українець"
a = 'Чехов {}'.format(b)
print(a)

6.2 уровень НУБ
answer1 = input('перша відповідь: ')
answer2 = input('друга відповідь: ')
string = 'Учора я написав ' + answer1 + ". " + 'Учора я ходив в ' + answer2 + "."
print(string)


6.2
answer1 = input('перша відповідь: ')
answer2 = input('друга відповідь: ')
answer3 = input('остання відповідь: ')
string = 'Я дуже люблю {}. Вчора я {} Юлю. Програмування - {}.'.format(answer1, answer2, answer3)
print(string)

6.3
born = 'олсдос Хаксли народився у 1894 році.'
born = born.capitalize()
print(born)
 метод title робить прописною перший символ першого слова після крапки
born = 'олсдос Хаксли народився у 1894 році. dsy.'
born = born.title()
print(born)
6.4
string = 'Де це?, Хто це?, Коли це?'.split(",")
print(string)


6.5
a = ['Руда', ' лисиця', 'перестрибнула', 'через', 'низький', 'паркан', '.']
a = ' '.join(a)
"""обимо зріз елементів від 0 до -2 і додємо крапку без відступів"""
a = a[0: -2] + "."
print(a)


6.6
a = """секс - це сенс мого життя,
хочу багато сексу з гарними дівчатами""".replace('е','Е')
print(a)


6.7
H = 'Хемінгуей'
print(H.index('м'))
'''
"""
6.8
a = '''Ігаль Левін розповів, де сконцентрують свої сили окупанти:
"Щоб ми думали, що наступатимуть на Слов'янськ"'''
print(a)
"""

6.9
a = 'три'
print(a+a+a)
print(a*3)

6.10
a = 'і не треба так кричати! я і вперший раз все почув.'
a = a.title()
a = a.split("!")
b = a[0]
print(b)
f = 'hello bitch) mayby sex?'
print(f[0: 11])

