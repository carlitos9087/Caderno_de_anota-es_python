def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): #antes da barra, entrada por posição, depois da barra pode usar parametros nomeados
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido


def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel): # aceita parametros de posição até a / e depois só parametros nomeados
    print(modelo, ano, placa, marca, motor, combustivel)

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  


def criar_carro(*, modelo, ano, placa, marca, motor, combustivel): # * só é aceito parametros nomeados
    print(modelo, ano, placa, marca, motor, combustivel)

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  #válido

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # O resultado da operação 10 - 10 = 0

###ta cheio de erro :(

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500
