# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

import wave



path = 'E:/WebDownload/wave/speak_recognize/home/aistudio/data/data51954/recordings/1_jackson_40.wav'
with wave.open(path, 'rb') as f:
    params = f.getparams()
    # 通道数、量化位数（byte）、采样率、采样帧数
    nchannels, samplewidth, framerate, nframes = params[:4]
    voiceStrData = f.readframes(nframes)
    # waveData = np.fromstring(voiceStrData, dtype=np.short)  # 将原始字符数据转换为整数
    waveData = np.frombuffer(voiceStrData, dtype=np.short)  # 将原始字符数据转换为整数
    # 音频数据归一化
    waveData = waveData * 1.0 / max(abs(waveData))
    print(waveData.shape)
    # 将音频信号规整成每行一路通道信号的格式，即该矩阵一行为一个通道的采样点，共nchannels行
    waveData = np.reshape(waveData, [nframes, nchannels]).T  # .T 表示转置
    print([nframes, nchannels])
    print(waveData.shape)

# 通过取样点数和取样频率计算出每个取样的时间。
print(np.arange(0,nframes))
print(framerate)
time = np.arange(0, nframes) * (1.0 / framerate)
plt.plot(time, waveData[0, :], c='b')
plt.xlabel('time')
plt.ylabel('am')
plt.show()

# numpy模块自带了快速傅里叶变换的函数
fftdata=np.fft.fft(waveData[0,:])
fftdata=abs(fftdata)
hz_axis=np.arange(0,len(fftdata))
plt.figure()
plt.plot(hz_axis,fftdata,c='b')
plt.xlabel('hz')
plt.ylabel('am')
plt.show()

# 使用matplotlib可以直接获得语谱图
plt.specgram(waveData[0],Fs = framerate, scale_by_freq = True, sides = 'default')
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
plt.show()


