peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))

imc = peso/altura**2

print(imc)

if imc < 17:
    print("Seu IMC é:", imc , "e está classificado como MUITO ABAIXO DO PESO")
elif 17 <= imc <= 18.49:  
    print("Seu IMC é:", imc , "e está classificado como ABAIXO DO PESO")
elif 18.5 <= imc <= 24.99:
    print("Seu IMC é:", imc , "e está classificado como PESO NORMAL")
elif 25 <= imc <= 29.99:
    print("Seu IMC é:", imc , "e está classificado como ACIMA DO PESO")
elif 30 <= imc <= 34.99:
    print("Seu IMC é:", imc , "e está classificado como OBESIDADE I")
elif 35 <= imc <= 39.99:
    print("Seu IMC é:", imc , "e está classificado como OBESIDADE II")
else:
    print("Seu IMC é:", imc , "e está classificado como OBESIDADE III")