import socket

def  start_server(host: str, port: int):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host,port))

    print(f'Server Started at {host}:{port} ')
    usuarios = {}

    while True:
        data, addr = server_socket.recvfrom(1024)

        name = data.decode('utf-8').split('!#')[0]
     

        print('Usuários conectados:')
        for user in usuarios.values():
            print('-', user)
        message = data.decode('utf-8').split('!#')[1]
        if addr not in usuarios:
            usuarios[addr] = name
            print(f'{name} entrou no chat')

        print(f'[{name}] diz: {message}')

        print(f'[{ name }] say: { message }')

if __name__=='__main__':
    HOST = '192.168.18.17'
    # HOST = 'localhost'
    PORT = 8000

    start_server(HOST, PORT)