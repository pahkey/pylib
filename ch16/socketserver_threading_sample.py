import socketserver
import random


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        answer = random.randint(1, 9)
        print(f'클라이언트가 접속했습니다:{self.client_address[0]}, 정답은 {answer} 입니다.')
        while True:
            data = self.request.recv(1024).decode('utf-8')
            print(f'데이터:{data}')

            try:
                n = int(data)
            except ValueError:
                self.request.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                continue

            if n == 0:
                self.request.sendall(f"종료".encode('utf-8'))
                break
            if n > answer:
                self.request.sendall("너무 높아요".encode('utf-8'))
            elif n < answer:
                self.request.sendall("너무 낮아요".encode('utf-8'))
            else:
                self.request.sendall("정답".encode('utf-8'))
                break


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 50007
    with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
