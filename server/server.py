import asyncio
import socket


class Server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._clients = {}

    def get_host_port(self) -> str:
        return f'{self._host}:{self._port}'

    async def handle_client(self, reader, writer):
        client_address = writer.get_extra_info('peername')
        print(f"Connection from {client_address}")

        writer.write('Enter username: '.encode())
        await writer.drain()

        username = (await reader.read(100)).decode().strip()
        self._clients[username] = writer

        try:
            while True:
                data = (await reader.read(100)).decode().strip()
                if not data:
                    break
                print(f"Received from {username}: {data}")
                await self.broadcast_message(f"{username}: {data}", username)
        except Exception as e:
            print(e)
        finally:
            del self._clients[username]
            print(f"Connection from {client_address} closed")

    async def broadcast_message(self, message, sender_username):
        for username, writer in self._clients.items():
            if username != sender_username:
                writer.write(f"{message}\n".encode())
                await writer.drain()

    async def start_server(self):
        serv = await asyncio.start_server(self.handle_client, host=self._host, port=self._port)
        print('server started')

        async with serv:
            await serv.serve_forever()
