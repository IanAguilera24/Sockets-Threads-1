import socket
import threading 


# configuración del servidor
HOST = '8.12.0.206'  # localhost
PORT = 3000        # puerto de escucha

# función que maneja las conexiones de los distintos clientes 

def manejo_cliente(conx, dir): 
    print('Conectado mediante', dir) 
    while True: 
        data = conx.recv(1024000)  # recibir datos del cliente 
        if not data: 
            break 
        print(f"Mensaje recibido del cliente {dir}: {data.decode('utf-8')}") 
        conx.sendall(data)  # enviar los mismos datos de vuelta al cliente 
    conx.close() 

# creación del socket 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT)) 
    s.listen()  # poner el socket en modo escucha 
    print('Servidor escuchando en', (HOST, PORT)) 
    while True: 
        conn, addr = s.accept()  # esperar una conexión 
        thread = threading.Thread(target=manejo_cliente, args=(conn, addr)) 
        thread.start() 
