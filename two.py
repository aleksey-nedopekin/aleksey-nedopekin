# лекция 1 задание 1
исходная_строка="axxlkxsasad dxaxx poaxthxx"
новая_строка = ""
for x in исходная_строка:
    if x == "x":
        новая_строка += "y"
    else:
        новая_строка += x
print(исходная_строка)
print(новая_строка)

# лекция 1 задание 2
числа = [1,2,3,4,5,6,15,4,4,4,5,3,7]
произведение = 1
for x in числа:
    if (x//5 == x/5 or x//3 == x/3):
        произведение *= x
print(произведение)

# лекция 1 задание 2
str='axxlkxsasad dxaxx poaxthxx'
исходная_строка = str.replace("x", "y")
print(исходная_строка)


#исходная_строка=str("axxlkxsasad dxaxx poaxthxx")
#исходная_строка = str.replace("x", "y")
#print(исходная_строка)


# лекция 2 задание 1 (описание списком)
I_am=['Недопёкин А.Е.', 'муж.', 'Россия', 'Пермь', 1985, 185, 75, 'инженер']
print(I_am)

# лекция 2 задание 2 (описание словарем)
I_am={'Недопёкин А.Е.':
      {'пол':'муж.','страна':'Россия','город':'Пермь','г.р.':1985,
      'доход по годам':{'2019':500, '2020':450,"2021":600}}}
print(I_am)

