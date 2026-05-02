import socket

def start_server(host: str, port: int):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f'Server Started at {host}:{port}')
    
    usuarios = {}

    while True:
        data, addr = server_socket.recvfrom(1024)
        decoded = data.decode('utf-8')

        name, message = decoded.split('!#', 1)

        if addr not in usuarios:
            usuarios[addr] = name
            print(f'{name} entrou no chat')

        if message.startswith('to'):
            partes = message.split(' ')

            if len(partes) >= 3:
                dest = partes[1]
                private = ' '.join(partes[2:])

                destino_addr = None

                for addr_user, nome_user in usuarios.items():
                    if nome_user == dest:
                        destino_addr = addr_user
                        break

                if destino_addr:
                    texto = f'[PRIVADO] {name}: {private}'
                    server_socket.sendto(texto.encode('utf-8'), destino_addr)
                else:
                    server_socket.sendto(f'Usuário {dest} não encontrado'.encode('utf-8'), addr)
     
        else:
            for user_addr in usuarios:
                texto = f'[{name}] {message}'
                server_socket.sendto(texto.encode('utf-8'), user_addr)

        print('\nUsuários conectados:')
        for user in usuarios.values():
            print('-', user)

        print(f'Total: {len(usuarios)} usuário(s)')
        print(f'[{name}] diz: {message}\n')


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8000

    start_server(HOST, PORT)