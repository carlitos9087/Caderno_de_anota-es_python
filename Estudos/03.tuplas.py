#________________TUPLAS____________
#__________________________________
from numpy import mat


tupla= ("laranja", "goiaba", "uva")
letras= tuple("python")
numeros= tuple([1,3,4])
pais=("brasil",)

print("\n"*2,type(tupla))
print("\n"*2,type(letras))
print("\n"*2,type(numeros))
print("\n"*2,type(pais))
print("\n"*2,type(""),"\n"*4)

matriz=(
    (1,"a",2),
    (2,"b",3),
    (30,"l",0)
)
print(matriz, sep="a")