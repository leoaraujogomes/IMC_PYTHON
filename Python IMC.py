p = float(input("Insira seu peso: "))
a = float(input("Insira sua altura: "))

imc = p/(a*a)

print("Seu IMC é: {:.1f}".format(imc))

categoria = ""
if (imc < 18.5):
    categoria = "Abaixo do peso"
elif ((imc >= 18.5) and (imc <= 24.9)):
    categoria = "Peso normal"
elif ((imc >= 25) and (imc <= 29.9)):
    categoria = "Sobrepeso"
elif ((imc >= 30) and (imc <= 34.9)):
    categoria = "Obesidade Grau I"
elif ((imc >= 35) and (imc <= 39.9)):
    categoria = "Obesidade Grau II"
elif (imc >= 40):
    categoria = "Obesidade Grau III ou Mórbida"

print("De acordo com o parâmetro da OMS, seu peso está classificado em:", categoria)