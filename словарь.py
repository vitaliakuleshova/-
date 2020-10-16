import sys
k=input()
b=input()
true1=0
true2=0
true3=0
true4=0

for i in range(len(k)):
    if "0"<=k[i]<="9":
        sys.exit("Неправильный ввод")
    else:
        if "a"<=k[i]<="z" or "A"<=k[i]<="Z":
            true1+=1
        elif "а"<=k[i]<="я" or "А"<=k[i]<="Я":
            true2+=1
for i in range(len(b)):
    if "0"<=b[i]<="9":
        sys.exit("Неправильный ввод")
    else:
        if "a"<=b[i]<="z" or "A"<=b[i]<="Z":
            true3+=1
        elif "а"<=b[i]<="я" or "А"<=b[i]<="Я":
            true4+=1

if true1==len(k) and true4==len(b):
    print("Aнглийское слово-",k)
    print("Русское слово-",b)
elif true2==len(k) and true3==len(b):
    print("Aнглийское слово-",b)
    print("Русское слово-",k)
else:
    print("Неправильно")

