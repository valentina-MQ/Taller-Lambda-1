from functools import reduce  # Importamos reduce desde functools

# Función lambda para calcular el factorial utilizando reduce
# La función lambda recibe un número z y aplica reduce para calcular su factorial
factorial = lambda z: reduce(lambda a, b: a * b, range(1, z + 1), 1)

# Solicitar al usuario un número entero
z = int(input("Ingrese un número entero: ")) 

# Se imprime el resultado del factorial calculado
print(f"El factorial de {z} es: {factorial(z)}")

""""
Explicación del código:

Se usa la función `lambda` para definir una función que calcula el factorial.
   
   - lambda a, b: a * b es la operación que multiplica cada número en la secuencia generada por range(1, z + 1).
   - reduce() se aplica esta operación de forma que se hace la multiplicación acumulativa, multiplicando 
     todos los números desde 1 hasta z.
   
 range(1, z + 1) genera una secuencia de números desde 1 hasta z, que se usa para calcular el factorial.
   - Ejemplo: Si z = 5, range(1, 6) genera [1, 2, 3, 4, 5].
   - reduce() multiplica secuencialmente estos números: 1 * 2 * 3 * 4 * 5 = 120.


"""