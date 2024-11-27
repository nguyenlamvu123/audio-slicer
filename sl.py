import librosa  # Optional. Use any library you like to read audio files.
import soundfile  # Optional. Use any library you like to write audio files.
import os
from pydub import AudioSegment

from slicer2 import Slicer


def cut_audio(file, i, ten_seconds=10 * 1000):
    song = AudioSegment.from_wav(file)
    leng = len(song)

    sta = 0
    ii = 0
    amountofloop = False
    while sta + ten_seconds < leng:
        fn = f"{os.path.splitext(file)[0]}___{ii}.wav"
        first_10_seconds = song[sta : sta + ten_seconds]
        first_10_seconds.export(fn, format="wav")
        sta += ten_seconds
        ii += 1
        if not amountofloop:
            amountofloop = True
    else:
        if not amountofloop:
            print()


dir = '/home/zaibachkhoa/Documents/convert2otherlang/so_vits_svc/crawl/ngoclan/separated/htdemucs/'
i = 0
for dir_ in os.listdir(dir):
    path = f'{dir}{dir_}{os.sep}vocals.wav'
    audio, sr = librosa.load(path, sr=None, mono=False)  # Load an audio file with librosa.
    slicer = Slicer(
        sr=sr,
        threshold=-40,
        min_length=5000,
        min_interval=300,
        hop_size=10,
        max_sil_kept=500
    )  # chia video dựa trên khoảng lặng
    chunks = slicer.slice(audio)
    for chunk in chunks:
        path_ = f'{dir_}_{i}.wav'
        if len(chunk.shape) > 1:
            chunk = chunk.T  # Swap axes if the audio is stereo.
        soundfile.write(path_, chunk, sr)  # Save sliced audio files with soundfile.
        cut_audio(path_, i)  # cắt nhỏ thành từng 10 giây
        os.remove(path_)
        i += 1