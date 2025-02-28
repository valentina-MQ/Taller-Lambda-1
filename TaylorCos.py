
import math

# Función lambda para calcular el factorial de un número
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Función lambda para calcular el polinomio de Taylor de cos(x)
taylor_cos = lambda x, n: sum(((-1)**k * x**(2*k)) / factorial(2*k) for k in range(n))

# Solicitar al usuario que ingrese los datos
x = float(input("Ingresa el valor de x (en radianes): "))
n = int(input("Ingresa el número de términos de la serie de Taylor: "))

# Calcular la aproximación de cos(x) usando el polinomio de Taylor
aprox_cos = taylor_cos(x, n)

# Calcular el valor real de cos(x) usando la función math.cos
real_cos = math.cos(x)

# Mostrar los resultados
print(f"Aproximación de cos({x}) usando {n} términos de la serie de Taylor: {aprox_cos}")
print(f"Valor real de cos({x}) usando math.cos: {real_cos}")
print(f"Diferencia entre la aproximación y el valor real: {abs(aprox_cos - real_cos)}")


"""
Calcula el factorial de un número n de manera recursiva. Esto es necesario para los coeficientes de la serie de Taylor.
Calcula la aproximación de cos(x) usando el polinomio de Taylor
La función lambda usa sum() para sumar los primeros n términos de la serie
Se llama a la función lambda taylor_cos para calcular la aproximación de cos(x)
Se calcula el valor real de cos(x) usando la función math.cos y se muestra la diferencia entre la aproximación y el valor real.

"""