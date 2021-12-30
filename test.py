import socket
from julius import Julius as J
julius=J()
host = 'localhost'   # IPアドレス
port = 10500         # Juliusとの通信用ポート番号
# Juliusにソケット通信で接続
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
data = ""
try:
    data = ""
    while True:
        if '</RECOGOUT>\n.' in data:
            # 出力結果から認識した単語を取り出す
            recog_text = ""
            for line in data.split('\n'):
                index = line.find('WORD="')
                if index != -1:
                    line = line[index+6:line.find('"', index+6)]
                    recog_text = recog_text + line
            print("認識結果: " + recog_text)
            data = ""
        else:
            data += str(client.recv(1024).decode('utf-8'))
            print('NotFound')
except KeyboardInterrupt:
    print('finished')
    client.send("DIE".encode('utf-8'))
    client.close()
