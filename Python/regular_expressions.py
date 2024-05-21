import re

def contar_correos_validos(archivo_texto):


  contador_correos = 0
  with open(archivo_texto, 'r') as f:
    for linea in f:
      # Expresión regular para identificar direcciones de correo electrónico
      regex =r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
      # Busca coincidencias en la línea actual
      coincidencias = re.findall(regex, linea)
      # Cuenta el número de coincidencias
      contador_correos += len(coincidencias)
  return contador_correos

# Ejemplo de uso
archivo_texto = "correos_ejemplo.txt"
numero_correos_validos = contar_correos_validos(archivo_texto)
print(f"Se encontraron {numero_correos_validos} correos electrónicos válidos")  
