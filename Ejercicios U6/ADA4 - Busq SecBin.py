import os
import hashlib

def hash_archivo(ruta_archivo):
    sha256 = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        while True:
            datos = f.read(4096)
            if not datos:
                break
            sha256.update(datos)
    return sha256.hexdigest()


def main():
    carpeta = input("Ingresa la ruta completa de la carpeta: ").strip()

    if not os.path.isdir(carpeta):
        print("La ruta NO es válida.")
        return

    print("\n=== HASH DE TODAS LAS SUBCARPETAS ===\n")

    # Recorre TODAS las carpetas y archivos
    for root, dirs, files in os.walk(carpeta):
        for archivo in files:
            ruta_completa = os.path.join(root, archivo)

            try:
                hash_valor = hash_archivo(ruta_completa)
                print(f"Archivo: {ruta_completa}")
                print(f"SHA-256: {hash_valor}\n")
            except Exception as e:
                print(f"No se pudo leer: {ruta_completa} -> {e}")


main()