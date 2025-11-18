#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the stored-waveform examples

from picodaq import *
import matplotlib.pyplot as plt
from scipy.signal import sweep_poly
import numpy as np
from code.cookbookhelper import showall

f0 = 10 * Hz
f1 = 100 * Hz
dur = 1 * s
fs = 10 * kHz

tt_s = np.arange(0, dur.as_('s'), (1/fs).as_('s'))
poly = [(f1-f0).as_('Hz') / dur.as_('s'), f0.as_('Hz')]
vv = sweep_poly(tt_s, poly, phi=-90)


def recipe_so1a():
    ##importall
    from scipy.signal import sweep_poly
    import matplotlib.pyplot as plt
    import numpy as np
    
    f0 = 10 * Hz
    f1 = 100 * Hz
    dur = 1 * s
    fs = 10 * kHz
    
    tt_s = np.arange(0, dur.as_('s'), (1/fs).as_('s'))
    poly = [(f1-f0).as_('Hz') / dur.as_('s'), f0.as_('Hz')]
    vv = sweep_poly(tt_s, poly, phi=-90)

    plt.plot(tt_s, vv)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    

def recipe_so1c():
    with AnalogOut(rate=fs) as ao:
        with AnalogIn(channel=0) as ai:
            ao[0].sampled(vv, scale=1*V)
            ao.run()
            data, times = ai.readall(times=True)

    plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    
    
showall(vars())
    
