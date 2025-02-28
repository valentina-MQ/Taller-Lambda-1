# Función lambda que implementa el algoritmo de Euclides 
mcd = lambda a, b: a if b == 0 else mcd(b, a % b)

# Solicitar al usuario que ingrese los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular el MCD utilizando la función lambda
resultado = mcd(num1, num2)

# Mostrar el resultado
print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")


"""
La expresión implementa el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos números (a y b). 
El algoritmo de Euclides se basa en la siguiente propiedad matemática:
El MCD de dos números a y b es igual al MCD de b y el residuo de la división de a entre b (es decir, a % b).
El proceso se repite hasta que el residuo (a % b) sea 0. Cuando esto ocurre, el MCD es el último valor no nulo de b.

"""