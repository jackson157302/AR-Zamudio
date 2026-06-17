"""
Taller No. 3 - Aplicación de buenas prácticas en codificación en Python
Automatización de Redes

Este programa realiza dos tareas principales:
1. Lista los archivos contenidos en el directorio de trabajo, mostrando
   nombre, extensión y ruta completa de cada uno.
2. Lee el archivo Usuarios.csv y muestra para cada usuario los campos
   Nombres, Apellidos, Dependencia, Estado y la cantidad total de
   columnas que tiene el registro.
"""

import os   # Módulo para interactuar con el sistema de archivos (rutas, listar directorios, etc.)
import csv  # Módulo para leer y escribir archivos CSV


# ---------------------------------------------------------------
# CONFIGURACIÓN / CONSTANTES
# ---------------------------------------------------------------

# Carpeta donde se encuentran los archivos del taller.
# os.path.abspath(__file__) obtiene la ruta completa de este script,
# y os.path.dirname() se queda solo con la carpeta que lo contiene.
# Así el programa funciona sin importar desde dónde se ejecute.
DIRECTORIO_TRABAJO = os.path.dirname(os.path.abspath(__file__))

# Nombre del archivo CSV que contiene la información de los usuarios
ARCHIVO_USUARIOS = "Usuarios.csv"


# ---------------------------------------------------------------
# FUNCIÓN 1: Listar archivos del directorio
# ---------------------------------------------------------------
def listar_archivos(directorio):
    """
    Recorre el directorio indicado y muestra, para cada archivo,
    su nombre, extensión y ruta completa.
    """
    print("=" * 50)
    print("LISTADO DE ARCHIVOS EN EL DIRECTORIO DE TRABAJO")
    print("=" * 50)

    # os.listdir() devuelve una lista con todos los elementos
    # (archivos y carpetas) que hay dentro del directorio
    for elemento in os.listdir(directorio):

        # Construye la ruta completa uniendo la carpeta + el nombre del elemento
        ruta_completa = os.path.join(directorio, elemento)

        # Solo procesamos archivos, no subcarpetas
        if os.path.isfile(ruta_completa):

            # os.path.splitext separa el nombre del archivo de su extensión
            # Ejemplo: "Usuarios.csv" -> ("Usuarios", ".csv")
            nombre, extension = os.path.splitext(elemento)

            print(f"Nombre     : {nombre}")
            print(f"Extensión  : {extension}")
            print(f"Ruta       : {ruta_completa}")
            print("-" * 50)


# ---------------------------------------------------------------
# FUNCIÓN 2: Leer y mostrar información de Usuarios.csv
# ---------------------------------------------------------------
def leer_usuarios(ruta_archivo):
    """
    Lee el archivo Usuarios.csv y muestra, para cada usuario,
    los campos Nombres, Apellidos, Dependencia, Estado y la
    cantidad total de columnas del registro.
    """
    print("=" * 50)
    print("INFORMACIÓN DE USUARIOS (Usuarios.csv)")
    print("=" * 50)

    try:
        # "with open(...)" abre el archivo y lo cierra automáticamente
        # al terminar el bloque, incluso si ocurre un error
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo_csv:

            # csv.reader convierte cada línea del archivo en una lista
            # de valores, separando por comas automáticamente
            lector = csv.reader(archivo_csv)

            # La primera fila contiene los nombres de las columnas
            # (encabezados), por ejemplo:
            # Cuenta, Nombres, Apellidos, Cargo, Dependencia, ...
            encabezados = next(lector)

            # En lugar de asumir un orden fijo de columnas, buscamos
            # la POSICIÓN de cada columna que necesitamos dentro de
            # la lista de encabezados. Esto hace el programa más
            # flexible si el orden de las columnas cambia.
            indice_nombres = encabezados.index("Nombres")
            indice_apellidos = encabezados.index("Apellidos")
            indice_dependencia = encabezados.index("Dependencia")
            indice_estado = encabezados.index("Estado")

            # Recorremos el resto de filas (cada una es un usuario)
            for fila in lector:

                # Si la fila está vacía (línea en blanco), la saltamos
                if not fila:
                    continue

                # Extraemos cada valor usando la posición encontrada arriba
                nombres = fila[indice_nombres]
                apellidos = fila[indice_apellidos]
                dependencia = fila[indice_dependencia]
                estado = fila[indice_estado]

                # len(fila) nos da el número total de columnas de ese registro
                total_columnas = len(fila)

                # Mostramos la información solicitada para este usuario
                print(f"Nombres        : {nombres}")
                print(f"Apellidos      : {apellidos}")
                print(f"Dependencia    : {dependencia}")
                print(f"Estado         : {estado}")
                print(f"Total columnas : {total_columnas}")
                print("-" * 50)

    # Si el archivo no existe, se captura el error y se muestra un mensaje claro
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta_archivo}'.")

    # Si alguna columna esperada (Nombres, Apellidos, etc.) no existe
    # en los encabezados, encabezados.index() lanza un ValueError
    except ValueError as error:
        print(f"Error: el archivo CSV no tiene la columna esperada -> {error}")


# ---------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ---------------------------------------------------------------
def main():
    """Función principal del programa."""

    # Paso 1: mostrar el listado de archivos de la carpeta de trabajo
    listar_archivos(DIRECTORIO_TRABAJO)

    # Paso 2: construir la ruta completa hacia Usuarios.csv
    ruta_usuarios = os.path.join(DIRECTORIO_TRABAJO, ARCHIVO_USUARIOS)

    # Paso 3: leer y mostrar la información de los usuarios
    leer_usuarios(ruta_usuarios)


# Este bloque asegura que main() solo se ejecute cuando el archivo
# se corre directamente (no cuando se importa desde otro script)
if __name__ == "__main__":
    main()
