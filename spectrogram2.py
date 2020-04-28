import sys
import numpy as np
import librosa
import matplotlib.pyplot as plt
#import scipy.io.wavfile
import librosa.display  # おニュー
"""
matplotlibの中にspecgram()という関数にもある
librosa（りぶろさ）は、音楽分析のためのPythonパッケージ。
スペクトル解析、テンポや拍子の分析、音楽の分析に必要な機能があらかじめ実装されてる
"""

args = sys.argv
wav_filename = args[1]
# ファイル読込
y, sr = librosa.load(wav_filename)

# 短時間フーリエ変換
S = np.abs(librosa.stft(y))

plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.amplitude_to_db(
    S, ref=np.max), y_axis='log', x_axis='time')
plt.title('Power spectrogram')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()
plt.show()
