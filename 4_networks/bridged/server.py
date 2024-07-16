import socket

def start_server():

    host = '0.0.0.0'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((host, port))
        s.listen()

        print("Socket Listening")

        conn, addr = s.accept()

        with conn:

            print(f"Contactado em: {addr}")

            while True:

                data = conn.recv(1024)
                if not data:
                    break
                print(f"Dados recebidos : {data.decode('utf-8')}")
                conn.sendall(data)


if __name__ == "__main__":
    start_server()