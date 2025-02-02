import sys
import time

def read_numbers_from_file(filename):
    """Lee números de un archivo, ignorando valores inválidos."""
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())  # Convertir a número flotante
                    numbers.append(number)
                except ValueError:
                    print(f"Datos inválidos ignorados: {line.strip()}")  # Manejo de errores
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        sys.exit(1)  # Terminar el programa con un error

    return numbers

def calculate_mean(numbers):
    """Calcula la media (promedio) de los números."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calcula la mediana de los números."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    """Calcula la moda (número más frecuente)."""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes if len(modes) < len(numbers) else "No mode"

def calculate_variance(numbers, mean):
    """Calcula la varianza de los números."""
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    """Calcula la desviación estándar."""
    return variance ** 0.5

def write_statistics_to_file(filename, statistics):
    """Guarda los resultados en un archivo."""
    with open(filename, 'w') as file:
        for key, value in statistics.items():
            file.write(f"{key}: {value}\n")

def main():
    """Función principal que ejecuta el programa."""
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        return

    input_file = sys.argv[1]
    print(f"Archivo recibido: {input_file}")

    start_time = time.time()  # Medir el tiempo de ejecución

    numbers = read_numbers_from_file(input_file)
    if not numbers:
        print("No hay números válidos en el archivo.")
        return

    # Cálculo de estadísticas
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_standard_deviation(variance)

    statistics = {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Standard Deviation": std_dev
    }

    # Mostrar resultados en pantalla
    for key, value in statistics.items():
        print(f"{key}: {value}")

    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")
    statistics["Elapsed Time"] = f"{elapsed_time:.4f} seconds"

    # Guardar en archivo
    write_statistics_to_file("StatisticsResults.txt", statistics)

if __name__ == "__main__":
    main()
