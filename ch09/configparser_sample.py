import configparser

config = configparser.ConfigParser()
config.read('ftp.ini')
ftp2_port = config['FTP2']['PORT']

print(ftp2_port)  # 22221 출력
