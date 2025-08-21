idade = int(input("Qual a sua idade?"))

if idade > 18 and idade <= 78:
    print("Você pode beber")
elif idade < 18:
    print("Você não pode beber")
elif idade == 79:
    print("É melhor você não beber: ")
elif idade >= 80 and idade <100: 
    print("Cara, melhor não beber, já te falei")

