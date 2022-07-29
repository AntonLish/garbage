import os

os.path.join("c", "users", "frt.txt")

f = open("frt.txt", "w")
f.write("функція write це те саме що print, тільки для файлів")
f.close

with open("frt.txt", "w") as g:
    g.write("функція write це те саме що print, тільки для файлів")
a = """write - видаляє все з файла і перезаписує нові данні
відповідно до послідовності коду в програмі"""

with open("frt.txt", "w") as f:
    f.write("""r(read) - читає файл,
            w(write) - записує в файл,
            W+(write+read) - читає і записує""")
    
#with open("frt.txt", "w") as f:
#    f.write("test of theory 'a'")

with open("frt.txt", "r") as f:
    print(f.read() + """
""" + a)

with open("frt.txt", "w") as f:
    f.write("""функція write це те саме що print, тільки для файлів,
            write - видаляє все з файла і перезаписує нові данні
            відповідно до послідовності коду в програмі, r(read) - читає файл,
            w(write) - записує в файл,
            W+(write+read) - читає і записує""")
            
my_list = []

with open("frt.txt", "r") as f:
    my_list.append(f.read())
print(my_list)

#9.2

with open("frt2.txt", "w") as f:
    a = input("""What is your name?
""")
    f.write(a)
with open("frt2.txt", "r") as f:
    print(f.read())
###########################################################################
    
import csv
with open("frt3.csv", "w") as h:
    h = csv.writer(h, delimiter = ",")
    h.writerow(["h - це об'єкт", "delimiter - додає потрібний нам розділювач"])
    h.writerow(["перебираєм об'єкти через цикл",
              """ за допомогою функції join
приєднуємо до кожного об'єкта кому ','"""])

with open("frt3.csv", "r") as h:
    h = csv.reader(h, delimiter = ",")
    for objects in h:
        print(",".join(objects))
########################################################################

#9.3
horror = ["Мама", "30 днів до світанку", "Прокляття"]
action = ["Термінатор", "Джон Уик", "Перевізник"]
classic = ["Матриц", "5 елемент", "Суддя Дред"]

cinema_list = [horror,action, classic]
 
with open("frt92.csv", "w") as c:
    c = csv.writer(c, delimiter = ".")
    for objects in cinema_list:
       c.writerow(objects)
       
with open("frt92.csv", "r") as c:
    c = csv.reader(c,delimiter = ".")
    for objects in c:
        print(objects)
# Відкриваємо файл frt92.csv для запису в перемінну с,
# передаємо наш файл і розділювач (в нашому випадку '.',
# може бути будь що).
# А ЩО САМЕ ГОЛОВНЕ ЗАВДЯКИ ПЕРЕБОРУ ЕЛЕМЕНТІВ ЗА ДОПОМОГОЮ ЦИКЛА
#МЕТОД WRITER ИКОНУЄТЬСЯ ДЛЯ КОЖНОГО ОБ'ЄКТА В СПИСКУ CINEMA_LIST
# І КОЖЕН СПИСОК З ФІЛЬМАМИ ВИВОДИТЬСЯ В НОВУ СТРОКУ
