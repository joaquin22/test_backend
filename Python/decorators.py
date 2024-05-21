import time

def tiempo_ejecucion(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()
        tiempo_ejecucion = end_time - start_time
        print(f"La función {func.__name__} tardó {tiempo_ejecucion:.2f} segundos en ejecutarse.")
        return resultado

    return wrapper

@tiempo_ejecucion
def ejemplo_funcion(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
        
    time.sleep(2.5)
    return suma

# Ejemplo de uso
ejemplo_funcion(100)