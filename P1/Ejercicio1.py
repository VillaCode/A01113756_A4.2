import sys

def main():
    # Verificar que el usuario proporcionó un archivo como argumento
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        return

    # Obtener el nombre del archivo desde los argumentos
    input_file = sys.argv[1]
    print(f"Archivo recibido: {input_file}")

if __name__ == "__main__":
    main()
