from server import Server


if __name__ == '__main__':
    print('start')
    server = Server('0.0.0.0', 90)
    server.start_server()
