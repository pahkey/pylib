import socket
import random

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버가 시작되었습니다.')
    conn, addr = s.accept()
    with conn:
        answer = random.randint(1, 9)
        print(f'클라이언트가 접속했습니다:{addr}, 정답은 {answer} 입니다.')
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(f'데이터:{data}')

            try:
                n = int(data)
            except ValueError:
                conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                continue

            if n == 0:
                conn.sendall(f"종료".encode('utf-8'))
                break
            if n > answer:
                conn.sendall("너무 높아요".encode('utf-8'))
            elif n < answer:
                conn.sendall("너무 낮아요".encode('utf-8'))
            else:
                conn.sendall("정답".encode('utf-8'))
                break
