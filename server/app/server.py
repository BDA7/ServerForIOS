import socket
import threading
import logging


class Server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._clients = {}
        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(__name__)

    def get_host_port(self) -> str:
        return f'{self._host}:{self._port}'

    def handle_client(self, client_socket, client_address):
        self._logger.info(f"Connection from {client_address}")

        try:
            client_socket.send('Enter username: '.encode())
            username = client_socket.recv(100).decode().strip()
            self._clients[username] = client_socket

            while True:
                data = client_socket.recv(100).decode().strip()
                if not data:
                    break
                self._logger.info(f"Received from {username}: {data}")
                self.broadcast_message(f"{username}: {data}", username)
        except Exception as e:
            self._logger.info(e)
        finally:
            client_socket.close()
            del self._clients[username]
            self._logger.info(f"Connection from {client_address} closed")

    def broadcast_message(self, message, sender_username):
        for username, client_socket in self._clients.items():
            if username != sender_username:
                client_socket.send(f"{message}\n".encode())

    def start_server(self):
        self._logger.info(f'Starting server on {self.get_host_port()}')
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self._host, self._port))
        server_socket.listen(5)

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

