    # Función lambda para definir la función matemática
    # Define la función matemática para la cual queremos encontrar la raíz.  f(x) = x³ - 2x - 5
funcion = lambda x: x**3 - 2*x - 5  

# Algoritmo de bisección usando una función lambda
biseccion = lambda f, n, m, tol: (
    ( n+ m) / 2 if abs(f((n + m) / 2)) < tol else  # Caso base: si el valor absoluto de f(c) es menor que la tolerancia
    biseccion(f, n, (n + m) / 2, tol) if f(n) * f((n + m) / 2) < 0 else  # Si hay un cambio de signo en [a, c]
    biseccion(f, (n + m) / 2, m, tol)  # Si hay un cambio de signo en [c, b]
)

# Solicitar al usuario que ingrese los datos
n = float(input("Ingresa el límite inferior del intervalo (n): "))
m = float(input("Ingresa el límite superior del intervalo (m): "))
tolerancia = float(input("Ingresa la tolerancia (por ejemplo, 0.0001): "))

# Verificar que la función tenga un cambio de signo en el intervalo [a, b]
if funcion(n) * funcion(m) >= 0:
    print("La función no tiene un cambio de signo en el intervalo dado. No se puede aplicar el método de bisección.")
else:
    # Aplicar el algoritmo de bisección
    raiz = biseccion(funcion, n, m, tolerancia)
    print(f"La raíz aproximada en el intervalo [{n}, {m}] es: {raiz}")