import requests
from jtalk import jtalk
from julius import Julius
import sys
import os
PREURL = 'https://apitest010.herokuapp.com/'
LOCALHOST='http://localhost:5000/'
END=['!','！','?','？','。']
# this URL is web api URL/<KEY>
if __name__ == "__main__":
    try:
        url=LOCALHOST
        response=requests.get(url+'こんばんは')
        
    except:
        url=PREURL
        if str(requests.get(url+'こんばんは')) == '<Response [503]>':
            print('herokuサーバの無料使用時間を使い切りました、来月までお待ちください')
            sys.exit(1)
    try:
        if sys.argv[1] == 'voice':
            jl = Julius()
            print('なにか喋って')
            flag=1
    except IndexError:
        flag=0
        pass
    while True:
        if flag == 1:
            try:
                text = jl.load()
                if text == '終わり。':
                    jl.end()
                    break
                elif text == '%NOT FOUND%':
                    continue
                else:
                    print('you:' + text)
            except KeyboardInterrupt:
                jl.end()
                break
        else:
            text = input('you:')
            if not text:
                break
        if not text[-1] in END:
            #コーパスは文末に毎回句読点を打ってるから
            text+='。'
        send = url+text
        response = requests.get(send)
        json_data = response.json()
        print('ai:'+json_data)
        jtalk(json_data)
