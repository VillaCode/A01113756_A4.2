"""
convert_numbers.py
Script que lee un archivo con números y los convierte a binario y hexadecimal.
Los resultados se imprimen en pantalla y se guardan en ConvertionResults.txt.
"""

import sys
import time

def decimal_to_binary(number):
    if number == 0:
        return "0"
    
    binary = ""
    is_negative = number < 0
    number = abs(number)

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    
    return "-" + binary if is_negative else binary

def decimal_to_hexadecimal(number):
    if number == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    is_negative = number < 0
    number = abs(number)

    while number > 0:
        hexadecimal = hex_digits[number % 16] + hexadecimal
        number //= 16

    return "-" + hexadecimal if is_negative else hexadecimal

def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r', encoding="utf-8") as file:  # Se especifica encoding
            for line in file:
                try:
                    number = int(line.strip())  # Convertir a entero
                    numbers.append(number)
                except ValueError:
                    print(f"Datos inválidos ignorados: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        sys.exit(1)

    return numbers

def write_conversions_to_file(filename, conversions, elapsed_time):
    with open(filename, 'w', encoding="utf-8") as file:  # Se especifica encoding
        file.write("Número Decimal | Binario | Hexadecimal\n")
        file.write("----------------------------------------\n")
        for original, binary, hexadecimal in conversions:
            file.write(f"{original} | {binary} | {hexadecimal}\n")
        file.write(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos\n")

def main():
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py fileWithData.txt")
        return

    input_file = sys.argv[1]
    print(f"Procesando archivo: {input_file}")

    start_time = time.time()

    numbers = read_numbers_from_file(input_file)
    if not numbers:
        print("No hay números válidos en el archivo.")
        return

    conversions = []
    for number in numbers:
        binary = decimal_to_binary(number)
        hexadecimal = decimal_to_hexadecimal(number)
        conversions.append((number, binary, hexadecimal))
        print(f"Decimal: {number}, Binario: {binary}, Hexadecimal: {hexadecimal}")

    elapsed_time = time.time() - start_time
    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")

    write_conversions_to_file("ConvertionResults.txt", conversions, elapsed_time)

if __name__ == "__main__":
    main()
