#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the stored-waveform examples

from code.cookbookhelper import showall

from picodaq import *
import psutil
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

f0 = 440 * Hz * 2**(-1 - 9/12) # C below middle C
fs = 48 * kHz

def getfreq():
    fnow, fmin, fmax = psutil.cpu_freq()
    return f0  * fnow / fmin

def produce():
    ph = 0
    t = 0*s
    N = 4096
    while True:
        f = getfreq()
        dph = (2 * np.pi * f / fs).plain()
        vv = np.sin(ph + dph*np.arange(N))
        ph = (ph + dph*N) % (2*np.pi)
        t += N/fs
        yield vv

        
def recipe_so2a():
    ##importall
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
                ttt.append(t)
    plt.plot(ttt, fff, '.-')
    plt.xlabel('Time (s)')
    plt.ylabel('Generated tone (Hz)')


    
def recipe_so2b():
    from picodaq.mockstim import mocksampled

    vvv = mocksampled(produce, scale=1*V, rate=fs, duration=10*s)
    plt.plot(vvv)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')
    plt.xlim(50000, 60000)
    

showall(vars())
    
