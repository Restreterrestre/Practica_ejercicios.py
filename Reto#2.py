#Este es el reto numero dos de ejercicios 

#Operadores

#Operadores aritmeticos

print("Suma:", 2+2)
print("Resta:", 4-2)
print("Multiplicacion:", 2*2)
print("Divicion:",10/3)
print("Modulo",10 % 3) #Devuelve lo que sobra despues de realizar la divicion entera
print("Potencia", 4**3)
print("Diviso con numero entero:",17//4)

#Operadores relacionales 

print("2 Mayor que 4", 2 > 4)
print("4 Mayor que 2", 4 > 2)
print(" 4 Menor que 2", 4 < 2)
print("2 Menor que 4", 2 < 4)
print("2 es igual 2", 2 == 2)
print("2 es igual a 5", 2 == 5)
print("Mayor igaul", 5 >= 7)
print("Menor igual ", 5 <= 7)
print("No son iguale 2 y 3", 2 != 3) #Mostrara verdadero si no son iguales en caso de ser iguales mostrara falso 

#Operadores de asignacion 

Variable = 1
print(Variable)
Variable = "Cambio a texto"
print(Variable)
Numero = 5
Numero += 5 
print(Numero)
Numero -= 3
print(Numero)
Numero *= 2
print(Numero)
Numero %= 3
print(Numero)
Numero /= 2
print(Numero)
Numero += 2
Numero **= 2
print(Numero)
Numero //= 2
print(Numero)
#Numero &= 2
#print(Numero)
#Numero |= 2
#print(Numero)
#Numero ^= 2
#print(Numero)
 
Nuevo_numero = 2
Nuevo_numero <<= 2
print(Nuevo_numero)

#Esta es una pruba del operador aritmetico modulo "%"
Modul = 17 % 3
Divizor_modul = 17/3
print("La division dio :",Divizor_modul)
print("El resultado del modulo es ",Modul)
#Operadores logicos 

Verdad = True
Mentira = False


print("Operador and: Verdadero,Falso:",Verdad and Mentira)#Solo devuelve true si los dos son true 

print("Operador and: Verdadero,Verdadero:",Verdad and Verdad)

print("Operador and: Verdadero,Falso:",Mentira and Mentira)

print("Operador or: Verdadero,Falso:",Verdad or Mentira) #Devuelve True si alguno de los operadores es verdad

print("Operador or: Falso,Falso:",Mentira or Mentira)

#Estructuras de control 
#Estructura if 

Condicion1 = 10
Condicion2 = 10

if Condicion1 == Condicion2 :
    print("Los numeros son iguales")
else:
    print("Los Numeros son diferentes")



a = 10
b = 30

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")

#Estructura for

numeros = [18,50,90,-20,100,80,37]
for n in numeros:
    print(n)





