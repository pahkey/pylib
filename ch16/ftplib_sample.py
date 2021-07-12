import ftplib

with ftplib.FTP(host='your_host_ip') as ftp:
    ftp.set_pasv(False)
    ftp.login(user='your_username', passwd='your_passwd')

    # FTP 서버의 data.txt 파일을 로컬 PC의 data.txt 파일로 다운로드한다.
    with open('data.txt', 'w') as save_f:
        ftp.retrlines("RETR data.txt", save_f.write)

    # data.txt 파일을 읽어 평균을 계산한다.
    with open('data.txt') as f:
        data = f.read()
        numbers = data.split()
        avg = sum(map(int, numbers)) / len(numbers)

    # 평균을 result.txt 파일에 기록한다.
    with open('result.txt', 'w') as f:
        f.write(str(avg))

    # result.txt 파일을 FTP 서버에 업로드한다.
    with open('result.txt', 'rb') as read_f:
        ftp.storlines("STOR result.txt", read_f)
