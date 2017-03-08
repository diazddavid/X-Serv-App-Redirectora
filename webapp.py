#!/usr/bin/python3

"""
webAppMulti class
Root for hierarchy of classes implementing web applications
Each class can dispatch to serveral web applications, depending
on the prefix of the resource name
Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles (2009-15)
jgb @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
October 2009, February 2015
"""

import socket

class webApp:

    def parse(self, request):
        """Parse the received request, extracting the relevant information.
        request: HTTP request received from the client
        """

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" +
                          "DUMB CODE" +
                          "</h1></body></html>")

    def __init__(self, hostname, port):
        """Initialize the web application."""

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048).decode('utf-8')
            print(request)
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()

if __name__ == "__main__":
    doWebApp = webApp("localhost", 1234)
