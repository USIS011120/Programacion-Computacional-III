
#Varibale de tipo cadena...
name = "Luis Hernandez"
print("Hola, mi nombre es " + name)

print( name[-2], type(name) )

#num1 = input("Dime un numero:") 
#num2 = input("Dime otro numero:")
#resp = float(num1) + float(num2)
#print(resp)

#10 NO, #15 
#respuesta = 7 - 4 + 5 * 2 + 2 / 2
#print(respuesta) #14-> 5*2=10 -> 7-4=3 -> 3+10=13 -> 2/2=1 -> 1+13=14

teGustaPython = True
print("Te gusta Python: "+ str(teGustaPython), type(teGustaPython))

#Calcular la edad de una persona
year = input("En que año naciste: ")
yearActual = 2021

def calcularEdad(year, yearActual):
    edad = yearActual - year
    return edad
print("Tu edad es: " + str(calcularEdad(int(year), yearActual)))