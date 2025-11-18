from picodaq import *
import psutil
import matplotlib.pyplot as plt
import numpy as np

f0 = 440 * Hz * 2**(-1 - 9/12) # C below middle C
fs = 48 * kHz

def getfreq():
    fnow, fmin, fmax = psutil.cpu_freq()
    return f0  * fnow / fmin

def produce():
    ph = 0
    t = 0*s
    N = 256
    while True:
        f = getfreq()
        dph = (2 * np.pi * f / fs).plain()
        vv = np.sin(ph + dph*np.arange(N))
        ph = (ph + dph*N) % (2*np.pi)
        t += N/fs
        yield vv

fff = []
ttt = []
t = 0
with AnalogOut(rate=fs) as ao:
    with AnalogIn(channel=0) as ai:
        ao[0].sampled(produce, scale=1*V)
        while t < 60:
            vv, tt = ai.read(0.25*s, times=True)
            pw = np.abs(np.fft.fft(vv))[:len(vv)//2]
            fff.append(fs.as_('Hz')*np.argmax(pw)/len(vv))
            t = np.mean(tt)
            print(t)
            ttt.append(t)
plt.plot(ttt, fff, '.-')
plt.xlabel('Time (s)')
plt.ylabel('Generated tone (Hz)')
