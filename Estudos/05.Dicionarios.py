############--------Dicionarios--------############
#como declarar dicionarios
nome= str
namorada= str

pessoa= {'nome':'bolsolula', 'idade': 12}
pessoa= dict(nome='sem nome', namorada="nulo", idade=900)#mudando valor da variavel pessoa
pessoa["teledone"]="11 96089-####"#adicionando telefone
print('\n',pessoa,'\n')

# agora que criamos nosso dicionario :( vamos substituir suas chaves
pessoa["nome"] = "carlitos"
pessoa['idade'] = 18
pessoa['namorada'] = 'continuo sem'

print('\n',pessoa,'\n')

#agora é a hora de coringar, dicionarios dentro de dicionarios... loucura, use banco de dados logo

contatos= {
"carlitos69@gmail.com": {"nome": 'carlos', 'idade': 18, 'telefone':12341234},
"carolzinha69@outlook.com": {"nome": 'carol', 'idade': 98, 'telefone':123456987},
"janaina_UwU_@gmail.com": {"nome": 'janaina', 'idade': 12, 'telefone':987654321}
}# depois de criar essa coisa feia, podemos acessar as informações como em uma matriz

print("\n", contatos["carlitos69@gmail.com"]["nome"])

for chave in contatos:# uma forma de mostrar o conteudo de uma matriz de dicionarios
    print(chave, contatos[chave])

for chave, valor in contatos.items():#outra forma de mostrar o conteudo de uma matriz de dicionarios
    print(chave, valor)

copia=contatos.copy()#copia a as informações
print(copia)
contatos.clear() #esse comando apaga... que surpresa 'O'
print(contatos)

#comando fromkeys
novo={}
novo=novo.fromkeys(["nome", "telefone"], "vaziooo")# cria dicionarios com varores "vazios"
print(dict.fromkeys(["nome", "telefone"]))#cria dicionarios com valores none
print(novo)

#comando get
print(novo.get("chave"))#verifica se existe a chave, como essa chave não existe, ele retorna none
print(novo.get("chave", "não existe essa chave"))#verifica e retorna uma mensagem se não existir
print(novo.get("nome", {}))#se existir ela não retorna nada, mas retornaria um dicionario vazio{}

#comando items() retorna tuplas
print(novo.items())

#comando keys() retorna só as chaves
print(novo.keys())

#comando pop() retorna o ultimo valor do dicionario e remove
novo.pop("nome")
print(novo) #se não achar, ele retorna {} vaxio

#popitem() retira o ultimo da pilha/dicionario
novo.popitem()
print(novo)

#setdefaut
novo.setdefault("nome","calica")#se não existir ele cria
print(novo)
novo.setdefault("nome","caliquinha")# se existir ele não altera
print(novo)
novo.setdefault("idade", 28)  # type: ignore
print(novo)

#comando update() atualiza seu dicionario
novo.update({"nome": "calicona", "idade": 8})# type: ignore
print(novo)

#comando values() retorna os valores
print(novo.values())

#in verifica a existencia de chaves
print("nome" in novo) # retorna um booleano

#del ele deleta
del copia['carlitos69@gmail.com']["nome"]
print(copia)
del copia['carlitos69@gmail.com']
print(copia)
del copia #deleta copia
