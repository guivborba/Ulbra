num1 = int(input("Primeiro núm: "))
num2 = int(input("Segundo núm: "))
num3 = int(input("Terceiro núm: "))

if num1 >= 0:
    print("A raíz quadrada do número 1 é: ",num1**0.5)
else:
    print("O quadrado do primeiro núemero é: ",num1**2)
if num2 > 10 and num2 < 100:
    print("O número está entre 10 e 100 - INTERVALO PERMITIDO")
else:
    print("O número não está entre 10 e 100 - INTERVALO NÃO PERMITIDO")
if num3 < num2:
    print("A diferença entre o número 3 e 2 é:" ,num2-num3)
else:
    print("A soma do número 2 e 3 é: ",num2+num3)
    
