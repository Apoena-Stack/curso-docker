import socket

def start_client():

    host = 'localhost'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((host,port))
        s.sendall(b"Hello Apoena, from docker_client.")
        data = s.recv(1024)
        
    print(f"Msg recebida do server: {data.decode('utf-8')}")

if __name__ == "__main__":

    start_client()