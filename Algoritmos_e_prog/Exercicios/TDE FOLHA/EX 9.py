num1 = int(input("Primeiro núm: "))
num2 = int(input("Segundo núm: "))
num3 = int(input("Terceiro núm: "))

if num1 > num2 and num1 > num3:
    print("O número 1 é o maior")
elif num1 < num2 and num2 > num3:
    print("O segundo número é o maior")
else:
    print("O terceiro número é o maior")