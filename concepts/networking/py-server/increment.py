import socket

HOST, PORT = '', 8888


def listen_socket_configuration():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    return listen_socket


def parse_request(text):
    request_line = text.splitlines()[0]
    request_line = request_line.rstrip('\r\n')
    # Break down the request line into components.
    return request_line.split()


if __name__ == '__main__':
    print 'Serving HTTP on port %s ...' % PORT
    listen_socket = listen_socket_configuration()
    counter = 0
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        parsed_request = parse_request(request)
        if (parsed_request[0] == 'POST' and parsed_request[1] == '/increment'):
            counter += 1
            http_response = "HTTP/1.1 200 OK\n"
            client_connection.sendall(http_response)
        if (parsed_request[0] == 'GET' and parsed_request[1] == '/increment'):
            http_response = "HTTP/1.1 200 OK\n\nCounter: %d\n" % counter
            client_connection.sendall(http_response)
        print request
        client_connection.close()
