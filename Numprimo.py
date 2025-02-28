# Función lambda para verificar si un número es primo
es_primo = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es primo usando la función lambda
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


"""
Un número es primo si solo es divisible por 1 y por sí mismo.
Asi que solo verificamos divisores desde 2 hasta la raíz cuadrada de n (int(n**0.5) + 1), ya que si 
no hay divisores en ese rango, no los habrá en rangos mayores.

La función all() asegura que todos los divisores en ese rango no dividan exactamente a n
Usa la función all() para comprobar si todos los números en el rango (2, int(n**0.5) + 1) no dividen 
exactamente a n (es decir, n % i != 0)
Si n es mayor que 1 y no es divisible por ningún número en ese rango, entonces es primo.

"""