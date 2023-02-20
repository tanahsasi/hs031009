#coding: utf-8
import subprocess
from datetime import datetime

def jtalk(t):
    # ���������̍쐬
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_bashful.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    # �����̓ǂݏグ
    aplay = ['aplay','-q','open_jtalk.wav'] #-Dhw:{�J�[�h�ԍ�},{�f�o�C�X�ԍ�}
    wr = subprocess.Popen(aplay)

def main():
    text = '�J�o��������'
    jtalk(text)

if __name__ == '__main__':
    main()
