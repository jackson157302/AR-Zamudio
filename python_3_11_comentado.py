import socket  # Módulo para trabajar con conexiones de red (sockets)

def servidor():
    host = "127.0.0.1"   # Dirección local (localhost = mi propia máquina)
    port = 5000          # Puerto donde el servidor va a escuchar conexiones

    # Crear un socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # "Amarra" el socket a la dirección IP y puerto definidos
    s.bind((host, port))

    # Pone el socket en modo escucha, aceptando como máximo
    # 1 conexión en espera (cola de conexiones pendientes)
    s.listen(1)
    print(f"Servidor escuchando en {host}:{port}...")

    # Espera (bloquea el programa) hasta que un cliente se conecte.
    # conn = nuevo socket para comunicarse con ese cliente
    # addr = dirección (IP, puerto) del cliente que se conectó
    conn, addr = s.accept()
    print(f"Conexión establecida con {addr}")

    # Bucle principal de conversación
    while True:
        # Recibe hasta 1024 bytes del cliente y los decodifica a texto
        data = conn.recv(1024).decode()

        # Si no llega nada, significa que el cliente cerró la conexión
        if not data:
            break

        print(f"Cliente dice: {data}")

        # El usuario del servidor escribe una respuesta
        mensaje = input("Servidor responde: ")

        # Envía la respuesta al cliente (codificada a bytes)
        conn.send(mensaje.encode())

    # Cierra la conexión con el cliente
    conn.close()

def cliente():
    host = "127.0.0.1"   # Dirección del servidor al que nos conectamos
    port = 5000          # Puerto del servidor

    # Crear un socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Se conecta al servidor (debe estar escuchando previamente)
    s.connect((host, port))

    # Bucle principal de conversación
    while True:
        # El usuario escribe un mensaje
        mensaje = input("Cliente escribe: ")

        # Envía el mensaje al servidor (codificado a bytes)
        s.send(mensaje.encode())

        # Espera y recibe la respuesta del servidor, la decodifica a texto
        data = s.recv(1024).decode()
        print(f"Servidor responde: {data}")

    # NOTA: esta línea nunca se ejecuta porque el bucle "while True"
    # no tiene una condición de salida (sería una mejora a futuro)
    s.close()

# Punto de entrada del programa: solo se ejecuta si corremos
# este archivo directamente (no si se importa como módulo)
if __name__ == "__main__":
    # Pregunta al usuario qué rol quiere tomar
    modo = input("¿Quieres iniciar como servidor (s) o cliente (c)? ").lower()

    if modo == "s":
        servidor()   # Inicia como servidor (debe ejecutarse primero)
    elif modo == "c":
        cliente()    # Inicia como cliente (se conecta al servidor)
    else:
        print("Modo inválido. Usa 's' o 'c'.")
