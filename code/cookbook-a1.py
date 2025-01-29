#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

from picodaq import *
import matplotlib.pyplot as plt
from code.cookbookhelper import showall


def recipe_a1a():
    ##importall
    import matplotlib.pyplot as plt

    with AnalogIn(channel=0, rate=50*kHz) as ai:
        data = ai.read(200*ms)

    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')

    
def recipe_a1b():
    with AnalogIn(channel=0, rate=50*kHz) as ai:
        data, times = ai.read(200*ms, times=True)

    plt.plot(times, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')

    
    
def recipe_a1c():
    with AnalogIn(channel=0, rate=50*kHz) as ai:
        data = ai.read(200*ms, raw=True)

    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Digital value')

def recipe_a1d():
    import numpy as np
    
    data = []
    times = []
    K = 25
    with AnalogIn(channel=0, rate=50*kHz) as ai:
        for k in range(K):
            dat, tms = ai.read(20*ms, times=True)
            print(f"Progress {k+1}/{K}", end="\r")
            data.append(dat)
            times.append(tms)
    print()
    data = np.concatenate(data, 0)
    times = np.concatenate(times, 0)

    plt.plot(times, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')

    
showall(vars())
    
