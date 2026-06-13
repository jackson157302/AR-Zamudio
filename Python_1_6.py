import socket
import argparse

# ------------------------------
# Ejercicio 1_6 - Socket Timeout
# ------------------------------

print("# ------------------------------")
print("# Ejercicio 1_6 - Socket Timeout")
print("# ------------------------------")

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Timeout por defecto
    print("Default socket timeout:", s.gettimeout())

    # Cambiar timeout a 100 segundos
    s.settimeout(100)
    print("Current socket timeout:", s.gettimeout())

    s.close()


# Ejecutar la función
test_socket_timeout()
