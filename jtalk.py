#coding: utf-8
import subprocess
import os
WIN=['./jtalk/bin/win/open_jtalk']
RASP=['./jtalk/bin/rasp/open_jtalk']
JIS='shift_jis'
UTF='utf-8'

def jtalk(t):
    if os.name=='nt':
        import winsound
        open_jtalk=WIN
        code = JIS
        mech = ['-x', 'jtalk/dic/win']
    else:
        open_jtalk = RASP
        code = UTF
        mech = ['-x', 'jtalk/dic/rasp']
    htsvoice = ['-m', 'voice/mei_normal.htsvoice']
    speed = ['-r', '1.0']
    outwav = ['-ow', 'open_jtalk.wav']
    cmd = open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE#,stderr=subprocess.PIPE
                         )
    c.stdin.write(t.encode(code))
    c.stdin.close()
    c.wait()
    if os.name == 'nt':
        winsound.PlaySound('open_jtalk.wav',winsound.SND_FILENAME)
    else:
        aplay = ['aplay', '-q', 'open_jtalk.wav']
        wr = subprocess.Popen(aplay)

if __name__ == "__main__":
    jtalk('お前はすでに死んでいる')
