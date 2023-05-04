import socket

# configuración del cliente
HOST = '8.12.0.250'  # localhost
PORT = 3000        # puerto del servidor

# creación del socket
cadena = input('Ingresa un mensaje')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(cadena.encode('utf-8'))
    #data = s.recv(1024)

print('Recibido:', cadena)
