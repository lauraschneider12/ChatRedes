import socket
import logging

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def start_server(host: str, port: int):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f'Server Started at {host}:{port}')
    logging.info(f'Server started at {host}:{port}')

    usuarios = {}

    while True:
        try:
            data, addr = server_socket.recvfrom(1024)
            decoded = data.decode('utf-8')

            if '!#' not in decoded:
                logging.warning(f'Mensagem inválida de {addr}: {decoded}')
                continue

            name, message = decoded.split('!#', 1)

            if addr not in usuarios:
                usuarios[addr] = name
                print(f'{name} entrou no chat')
                logging.info(f'{name} entrou no chat - {addr}')

            if message.startswith('to '):
                partes = message.split(' ')

                if len(partes) >= 3:
                    dest = partes[1]
                    private = ' '.join(partes[2:])

                    destino_addr = None

                    for addr_user, nome_user in usuarios.items():
                        if nome_user.lower() == dest.lower():
                            destino_addr = addr_user
                            break

                    if destino_addr:
                        texto = f'[PRIVADO] {name}: {private}'
                        server_socket.sendto(texto.encode('utf-8'), destino_addr)
                        logging.info(f'PRIVADO {name} -> {dest}: {private}')
                    else:
                        erro = f'Usuário {dest} não está online'
                        server_socket.sendto(erro.encode('utf-8'), addr)
                        logging.warning(f'{name} tentou enviar para {dest}, mas não encontrou')
                else:
                    server_socket.sendto('Use: to nome mensagem'.encode('utf-8'), addr)

            else:
                for user_addr in usuarios:
                    if user_addr != addr:
                        texto = f'[{name}] {message}'
                        server_socket.sendto(texto.encode('utf-8'), user_addr)

                logging.info(f'MSG {name}: {message}')

            print('\nUsuários conectados:')
            for user in usuarios.values():
                print('-', user)

            print(f'Total: {len(usuarios)} usuário(s)')
            print(f'[{name}] diz: {message}\n')

        except Exception as e:
            logging.error(f'Erro no servidor: {e}')
            print(f'Erro: {e}')


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8000

    start_server(HOST, PORT)