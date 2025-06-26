name="Иван"
print(name)
a=10
b=5
print(a+b)
num=11
print(str(num) + "число для проверки")
if num % 2 ==0:
    print("Четное")
else:
    print("Нечетное")
age = int(input("Введите возраст"))
if age <12 :
    print("Kids")
else: 
    if age>=12 and age<18:
        print("tenager")
    else:
        if age>18:
            print("Big boy")
#Задача 5(вообще я гуглил синтаксис, но как решить понял сразу) хмм почему-то вывод идет с 0
i=1
for i in range(6):
    print("Число:"+str(i))
#Задача 6 схитрожопил
i=6
while i>1:
    if i==4:
        i-=2
    else:
        i-=1
    print(i)
#задача 7 
def power(x,y):
    return x**y
print(power(2,3))
#задача 8 показывает ошибку в коде, ну я бы тоже решил хз только как записать if в функцию(я гуглю синтаксис и не нашел что-то такого)
def is_positive(z):
    return if z>0
    print("")