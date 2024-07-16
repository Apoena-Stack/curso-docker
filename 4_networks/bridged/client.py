import socket

def start_client(server_ip):

    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((server_ip,port))
        s.sendall(b'Hello, Apoena!')
        data = s.recv(1024)

    print(f"Msg recebida de volta: {data.decode('utf-8')}")


if __name__ == "__main__":
    
    start_client("apoena-server")
    
    
