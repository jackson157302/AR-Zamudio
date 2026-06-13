import socket      # Módulo para trabajar con conexiones de red (sockets)
import argparse    # Módulo para argumentos de línea de comandos (no se usa en este script)

# ------------------------------
# Ejercicio 1_6 - Socket Timeout
# ------------------------------

# Imprime un encabezado decorativo en la consola
print("# ------------------------------")
print("# Ejercicio 1_6 - Socket Timeout")
print("# ------------------------------")

def test_socket_timeout():
    # Crea un socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Muestra el timeout por defecto del socket.
    # Por defecto es "None", es decir, el socket es BLOQUEANTE
    # (esperaría indefinidamente si no recibe respuesta)
    print("Default socket timeout:", s.gettimeout())

    # Cambia el timeout del socket a 100 segundos.
    # A partir de aquí, si el socket intenta conectarse, enviar
    # o recibir datos y nadie responde, lanzará un error
    # "socket.timeout" después de 100 segundos
    s.settimeout(100)
    print("Current socket timeout:", s.gettimeout())

    # Cierra el socket y libera el recurso
    s.close()


# Ejecutar la función para ver el resultado
test_socket_timeout()
