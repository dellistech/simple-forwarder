import socket
import argparse
import sys


parser = argparse.ArgumentParser()

parser.add_argument("lport", help="TCP Port to set up listener", default=8081)
#parser.add_argument("fport", help="TCP Port to forward from.", default=8081)

args = parser.parse_args()


port = int(args.lport)

def main():
    # Setup the socket and listen 
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    ServerSocket.bind(('', port))
    ServerSocket.listen()

    while True:
        try:
            #accept connection
            conn, addr = ServerSocket.accept()
            data = conn.recv(4096)
            # fork
            print(data.decode('utf-8'))

        except KeyboardInterrupt:
            ServerSocket.close()
            print("Received Keyboard Interrupt. Exiting...")
            sys.exit(1)


if __name__ == '__main__':
    main()