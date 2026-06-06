import socket

def servidor():
    host = "127.0.0.1"   # Dirección local
    port = 5000          # Puerto de escucha

    # Crear socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Servidor escuchando en {host}:{port}...")

    conn, addr = s.accept()
    print(f"Conexión establecida con {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Cliente dice: {data}")
        mensaje = input("Servidor responde: ")
        conn.send(mensaje.encode())

    conn.close()

def cliente():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        mensaje = input("Cliente escribe: ")
        s.send(mensaje.encode())
        data = s.recv(1024).decode()
        print(f"Servidor responde: {data}")

    s.close()

if __name__ == "__main__":
    modo = input("¿Quieres iniciar como servidor (s) o cliente (c)? ").lower()
    if modo == "s":
        servidor()
    elif modo == "c":
        cliente()
    else:
        print("Modo inválido. Usa 's' o 'c'.")
