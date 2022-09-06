num1 = int(input("Primeiro núm: "))
num2 = int(input("Segundo núm: "))

resto1 = num1%2
resto2 = num2%2

if resto1 == 0:
    print("O primeiro número é múltiplo de 2")
else:
    print("O primeiro número não é múltiplo de 2")
if resto2 == 0:
    print("O segundo número é múltiplo de 2")
else:
    print("O segundo número não é múltiplo de 2")
