import socket

def start_client(host: str, port: int):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    name = input('Seu nome: ')

    while True:
        msg = input('Mensagem: ')
        mensagem = f'{name}!#{msg}'
        client_socket.sendto(mensagem.encode('utf-8'), (host, port))


if __name__ == '_main_':
    HOST = 'localhost'  # usa o mesmo do server
    PORT = 8000

    start_client(HOST, PORT)