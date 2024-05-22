import re


def count_valid_emails(file_text):

    email_count = 0
    with open(file_text, "r") as f:
        for linea in f:
            # Expresión regular para identificar direcciones de correo electrónico
            regex = r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"

            matches = re.findall(regex, linea)
            email_count += len(matches)
    return email_count


# Ejemplo de uso
file_text = "correos_ejemplo.txt"
number_of_valid_emails = count_valid_emails(file_text)
print(f"Se encontraron {number_of_valid_emails} correos electrónicos válidos")
