# a = 4
# b= 6
# resultado =0

# for x in range(b):
#     resultado += b
# print(resultado)

# nombre = 'Chanchito'
# Apellido = 'Feliz'

# contat = nombre+ ' ' + Apellido

# print(contat[::-1]) #::-1 es para darle vuelta a un numero

# lista = [1,2,5,-6,23,43,53]
# menor = 'init'
# for num in lista:
#     if menor =='init':
#         menor = num
#     else:
#         menor = num if num < menor else menor
# print(menor)

# def calcular_volumen(r):
#     return 4/3 * 3.1416 * r **3


# print(calcular_volumen(6))

# def EsMayor(usuario):
#     return usuario.edad > 17

# class Usuario:
#     def __init__(self,edad, Nombre, apellido):
#         self.edad = edad
#         self.nombre = Nombre
#         self.Apellido = apellido


# usuario = Usuario("24","Lidys", 'Fugon')# Mira yo del futuro esto recib
# # Carlos = Usuario(15)
# # Juan = Usuario(21)

# print('La edad de '+ usuario.nombre+ ' '+usuario.Apellido+ ' es: ', usuario.edad)

MiPrimerString = 'Mi nombre es Lidys Fugon tengo 24 años y voy hacer mama'

for c in MiPrimerString:
    print(c)
    

print(MiPrimerString)
print(len(MiPrimerString))

# print(EsMayor(usuario1), EsMayor(usuario2))

# def Espar(A):
#     return A%2 ==0

# print(Espar(3))

# palabra = 'ChanchitoFeliz'
# vocales = 0

# for c in palabra:
#     y = c.lower()
#     vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y== 'u' else 0

# print(vocales)
# lista = []
# print('ingrese numeros y para salir escriba "Basta"')
# while True:
#     valor = input('Ingrese valor: ')
#     if valor == 'Basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato Invalido')
#             exit()

# resultado = 0

# for x in lista:
#     resultado += x

# print(resultado)
# #import os as

# def AgregarNombres(nombre, apellido):
#     c = open('Nombrecompleto.txt','a')
#     c.write(nombre+' '+ apellido+'\n')
#     c.close

# AgregarNombres('Rodrigo','Bonilla')
