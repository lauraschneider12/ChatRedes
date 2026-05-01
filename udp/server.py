import socket

def start_server(host: str, port: int):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f'Server Started at {host}:{port}')
    
    usuarios = {}

    while True:
        data, addr = server_socket.recvfrom(1024)
        decoded = data.decode('utf-8')

        name, message = decoded.split('!#')

        
        if addr not in usuarios:
            usuarios[addr] = name
            print(f'{name} entrou no chat')

       
        print('\nUsuários conectados:')
        for user in usuarios.values():
            print('-', user)

        print(f'Total: {len(usuarios)} usuário(s)')

      
        print(f'[{name}] diz: {message}\n')

if __name__ == '_main_':
    HOST = 'localhost'
    PORT = 8000

    start_server(HOST, PORT)