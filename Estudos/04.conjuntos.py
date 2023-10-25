#---------conjuntos------------#
o=set([1,2,3,4,5,6,7,8,9,1,2,3,4,5])
ai=set(["celta", "camila","celta", "camila", "uruguai"])
oi={"oi","oi","java","oi"}

""" print(oi)
for a in ai:
    print(a, end=(" ")) """

ui= ai.union(oi) #une as duas variáveis
print(ui)

ei= ai.intersection(oi)#retorna a intersecção
print(ei)

ii= oi.difference(ai)#retorna a diferença
print(ii)

diferenca_cimetrica = ai.symmetric_difference(oi)# retorna tudo que não esteja na intersecção
print(diferenca_cimetrica)

oia= oi.issubset(ai)#retorna true ou false, se o primeiro esta contido no segundo
print(oia)

ooo= oi.issuperset(ai)#retorna true ou false, se o primeiro contem o segundo
print(ooo)

aaa= oi.isdisjoint(ai)#etorna true ou false, se os dois conjuntos não se tocarem
print(aaa)

#comando add no set

carro={"mustang", "fiat", "não sei nome de carro fds"}
carro.add("ae")
print(carro)

#copy copia
a=carro.copy()
print(a)
#comando clear (limpa seu set)
carro.clear()
print(carro)
#comando discart
o.discard(1)
print(o)
#pop pilha
o.pop()
print(o)
#remove ele remove
o.remove(3)
print(o)
#comando in para saber se algo esta em algo

print(5 in o)