from operacoes.operacoes import soma, subtracao, divisao, multiplicacao

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

resultado_soma = soma(num1, num2)
resultado_subtracao = subtracao(num1, num2)
resultado_divisao = divisao(num1, num2)
resultado_multiplicacao = multiplicacao(num1, num2)

print(f"Soma: {resultado_soma}")
print(f"Subtração: {resultado_subtracao}")
print(f"Divisão: {resultado_divisao}")
print(f"Multiplicação: {resultado_multiplicacao}")