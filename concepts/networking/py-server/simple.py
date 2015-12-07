import socket

HOST, PORT = '', 8888


def listen_socket_configuration():
    # AF_INET is the address family that our socket can communicate with,
    # and SOCK_STREAM is the socket type -- provides a connection-oriented,
    # sequenced, and unique flow of data w/o record boundaries.
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Associate the socket with its local address. Clients can use this address
    # to connect to the server. That is, bind defines the communication endpoint
    listen_socket.bind((HOST, PORT))
    # Listen for connections made to the socket -- the argument specifies the
    # max number of queued connections.
    listen_socket.listen(1)
    return listen_socket


if __name__ == '__main__':
    print 'Serving HTTP on port %s ...' % PORT
    listen_socket = listen_socket_configuration()
    while True:
        # Accept a connection. Can call accept on a socket that is bound to
        # an address and listening for connecitons. Return val is a pair,
        # (client_connection, client_address), where client_connection is a
        # new socket object usable to send a receive data on the connection, and
        # client_address is the address bound to the socket on the other end
        # of the connection
        client_connection, client_address = listen_socket.accept()
        # Receive data from the socket -- return value is a string representing
        # data received. This is gonna be the stuff that's printed in the
        # terminal. The client (in our case, browser or cURL) makes a request
        # and sends a bunch of metadata along with the request. That metadata
        # is printed to the terminal.
        request = client_connection.recv(1024)
        print request

        http_response = """\
            HTTP/1.1 200 OK

            Hello, World!
            """
        # Send the response to the client. In this case, text that says hello
        # world.
        client_connection.sendall(http_response)
        client_connection.close()
