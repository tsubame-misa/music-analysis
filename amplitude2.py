import wave
from numpy import *
from pylab import *
import sys


def printWaveInfo(wf):
    """WAVEファイルの情報を取得"""
    print("チャンネル数:"+str(wf.getnchannels()))
    print("サンプル幅:"+str(wf.getsampwidth()))
    print("サンプリング周波数:"+str(wf.getframerate()))
    print("フレーム数:"+str(wf.getnframes()))
    print("パラメータ:"+str(wf.getparams()))
    print("長さ（秒）:"+str(float(wf.getnframes()) / wf.getframerate()))


if __name__ == '__main__':
    args = sys.argv
    wav_filename = args[1]
    wf = wave.open(wav_filename, "r")
    printWaveInfo(wf)

    buffer = wf.readframes(wf.getnframes())
    print(len(buffer))  # バイト数 = 1フレーム2バイト x フレーム数

    # bufferはバイナリなので2バイトずつ整数（-32768から32767）にまとめる
    data = frombuffer(buffer, dtype="int16")

    # プロット
    plot(data[0:1000])
    show()
