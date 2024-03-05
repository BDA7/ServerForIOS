from server.server import Server
import asyncio

if __name__ == '__main__':
    server = Server('127.0.0.1', 12345)
    asyncio.run(server.start_server())