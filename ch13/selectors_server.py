import socket
import selectors
import random

HOST = ''
PORT = 50007

sel = selectors.DefaultSelector()  # 최적의 Selector를 생성한다.
answers = {}


def accept_client(sock):
    """ 서버 소켓에 클라이언트가 접속하면 호출된다. """
    conn, addr = sock.accept()
    answer = random.randint(1, 9)
    answers[conn] = answer
    sel.register(conn, selectors.EVENT_READ, game_client)  # 클라이언트 소켓을 등록한다.
    print(f'클라이언트가 접속했습니다:{addr}, 정답은 {answer} 입니다.')


def game_client(conn):
    """ 클라이언트 소켓에 데이터가 수신되면 호출된다. """
    data = conn.recv(1024).decode('utf-8')
    print(f'데이터:{data}')
    try:
        n = int(data)
        answer = answers.get(conn)
        if n == 0:
            conn.sendall(f"종료".encode('utf-8'))
            sel.unregister(conn)
            conn.close()
        elif n > answer:
            conn.sendall("너무 높아요".encode('utf-8'))
        elif n < answer:
            conn.sendall("너무 낮아요".encode('utf-8'))
        else:
            conn.sendall("정답".encode('utf-8'))
            sel.unregister(conn)
            conn.close()
    except ValueError:
        conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버가 시작되었습니다.')
    sel.register(s, selectors.EVENT_READ, accept_client)  # 서버 소켓을 등록한다.

    while True:
        events = sel.select()  # 클라이언트의 접속 또는 접속된 클라이언트의 데이터 요청을 감시
        for key, mask in events:
            callback = key.data  # 실행할 함수
            callback(key.fileobj)  # 이벤트가 발생한 소켓을 인수로 실행할 함수를 실행한다.
