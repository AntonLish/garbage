'''5.1'''
bands = ["slipknot", "rammstein", "garbage"]

'''5.2'''
locations = [(23,23,), (21,21,), (34,34,)]

'''5.3'''
im = {"growth":"175 cm", "color":"black", 
        "band":"rammstein"}

'''5.4'''
n = input("введіть запрос: ")
if n in im:
    z = im[n]
    print(z)
else:
    print("не знайдено")
    
'''5.5'''
a = ["sulfur", "sic", "vermilion"]
b = ["sonne", "mutter", "benzin"]
c = ["queer", "control", "sugar"]

playlist = {"slipknot": a, "rammstein":b, "garbage":c}

j = input("введіть виконавця: ")
if j in playlist:
    d =  playlist[j]
    print(d)
else:
    print("не знайдено")
