import socket
import threading

def receber(client_socket):
    while True:
        data, _ = client_socket.recvfrom(1024)
        print('\n' + data.decode('utf-8'))

def start_client(host: str, port: int):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_socket.bind(('0.0.0.0', 0))

    name = input('Seu nome: ')

    threading.Thread(target=receber, args=(client_socket,), daemon=True).start()

    while True:
        msg = input('Mensagem: ')
        mensagem = f'{name}!#{msg}'
        client_socket.sendto(mensagem.encode('utf-8'), (host, port))


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8000

    start_client(HOST, PORT)