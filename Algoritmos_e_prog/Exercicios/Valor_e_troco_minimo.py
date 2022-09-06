número = int(input("Digite o valor: R$"))

print("O valor mínimo de notas é: ")

cem = int(número/100)
número = número - (cem*100)

cinquenta = int(número/50)
número = número - (cinquenta*50)

vinte = int(número/20)
número = número - (vinte*20)

dez = int(número/10)
número = número - (dez*10)

cinco = int(número/5)
número = número - (cinco*5)

dois = int(número/2)
número = número - (dois*2)

um = int(número/1)
número = número - (um*1)

if cem > 0:
    print(cem, "Nota(s) de cem")
if cinquenta > 0:    
    print(cinquenta, "Nota(s) de Cinquenta Reais")
if vinte > 0:    
    print(vinte, "Nota(s) de Vinte Reais")
if dez > 0:
    print(dez, "Nota(s) de Dez Reais")
if cinco > 0:
    print(cinco, "Nota(s) de Cinco Reais")
if dois > 0:
    print(dois, "Nota(s) de Dois Reais")
if um > 0:
    print(um, "Moeda(s) de Um Real")

