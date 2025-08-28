salario = float(input("Insira o valor do seu salário: "))
carteira = input("Você possui mais de 3 anos de carteira assinada? (sim/não)").strip().lower()


if salario >= 1500 and carteira == "sim":
    print("Seu subsidio será de R$ 45.000,00")

elif salario <= 1500 and carteira =="sim": 
    print("Seu subsidio será de R$ 22.500,00")

elif salario <= 1500 and carteira =="não":
    print("Não terá valor de subsidio disponivel")

else: salario >= 1500 and carteira =="não"
print("Seu subsidio será dee R$ 22.500,00")