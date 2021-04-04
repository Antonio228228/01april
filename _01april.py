#Anton Slepnjov TITpv20
numbers=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Programeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список")
    print("2-cклеить списки\n3-добавить букву на i - позицию")
    print("4-удалить букву\n5-удалить его порядковый номер")
    print("6-узнать позицию элемента")
    print("7-переворот")
    valik=int(input())
    if valik==1:
        a=input("Введи букву")
        slovo_list.append(a)
        print(f"Добавили {a} новый список",slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить")
        i=int(input("Введи номер позиции, куда хочешь добавить"))
        slovo_list.insert(i-1,a)
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить")
        n=slovo_list.count(a)
        print(n)
        if n>0:
            for i in range(n):
                slovo_list.remove(a)
        else:
            print("Такой буквы нет")
            print(slovo_list)
    elif valik==5:
        i=int(input("Введи номер позиции элемента для удаления"))
        n=len(slovo_list)
        if i<n:
            slovo_list.pop(i)
            print(slovo_list)
        else:
            print("Букв мень чем указаная позиция")
    elif valik==6:
        a=input("Введи букву, позицию которой хочешь узнать")
        i=slovo_list.index(a)
        print(f"Элемент {a} стоит на {i+1}-ом месте")
    elif valik==7:
        slovo_list.reverse()
        print(slovo_list)

#Anton Slepnjov TITpv20 dz
txt = "one two three FOUR FIVE"
x = txt.swapcase()
print(x)
#

txt2 = "my name is anton"
z = txt2.capitalize()
print (z)
#

txt3 = "     banana     "
c = txt3.lstrip()
print("of all fruits", c, "is my favorite")
#

txt4 = "     orange     "
v = txt4.rstrip()
print("of all fruits", v, "is my favorite")
#

txt5 = "     grapefruit     "
b = txt5.strip()
print("of all fruits", b, "is my favorite")
#

txt6 = "Hello, my name is Anton."
n = txt6.startswith("Hello")
print(n)
#

q = chr(97)
print(q)
#

txt7 = "50"
w = txt7.zfill(10)
print(w)
#

txt8 = "   "
e = txt8.isspace()
print(e)
#

txt9 = "SpaceX"

y = txt9.isalpha()

print(y)
#