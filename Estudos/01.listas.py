import os

curso = "  PyThon"
print("+".join(curso))
'''
print(curso.lower())
print(curso.upper())
print(curso.strip())
print("+".join(curso))
print(curso.lstrip().rstrip().center(11,"-"))
print(curso.title(),"\n\n\n")
print(curso[:10]) '''

""" nome = 'carlos'
print(f'''
o nome de quem escreveu esse código
é {nome}, e ele está aprendendo python
'''

print(nome[::-2])
 """

""" entrada = input().split()
print(entrada)
distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

icm = (distancia / (diametro1 + diametro2))
print(f'{icm: .2f}')  """

""" print("digite respectivamente o numero de cachorros quentes e o numero de participantes")
valores = input().split() 
H= int(valores[0])
P= int(valores[1])
media= (H/P)
print(f'{media:.2f}') """
'''
valores = input().split()
#12km/l
tempo = int(valores[0])
velocidade = int(valores[1])
litros= (tempo*velocidade)/12
print(f'{litros:.3f}')
'''
# os.system('clear') #limpa a tela

a=[] 
lista=["cosmo",1,"celta", "fatec", 12.8, ["bonet", "cosminho", "python"]]
copia_da_lista = lista.copy()
copia_da_lista[1:6] = ["a","b","c"] 
# a.extend(copia_da_lista) 
# print(a,"\n"*5)
# print(lista.index("celta"))
# print(copia_da_lista.count(""))

""" for i in range(0,len(lista)): 
    a.append(lista.pop())
    print(a)
 """
# a=lista.pop()
# a=lista.pop()
# lista.pop()
# lista.pop()
# lista.pop() #pilha
# print(a)
# print(lista.remove(1)) #remove
# print (lista)
# print(lista.reverse()) #inverte a ordem
print(copia_da_lista)
copia_da_lista.sort(reverse=False)
print(copia_da_lista)
copia_da_lista.sort(reverse=True)
print(copia_da_lista)
# copia_da_lista.sort(key=lambda oi: len(oi))
# print(copia_da_lista)
# sorted(lista, key=lambda y: len(y))
for alvo, carro in enumerate(copia_da_lista):
    print(alvo, carro)

oi=[]
for i in range(3):
    print(f"digite o {i+1}° numero")
    
    oi.append(input(""))
    print(oi)