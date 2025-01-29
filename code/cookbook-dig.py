#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

from picodaq import *
import matplotlib.pyplot as plt
from code.cookbookhelper import showall


def recipe_d1a():
    ##importall
    import matplotlib.pyplot as plt

    with DigitalIn(line=0, rate=50*kHz) as di:
        data = di.read(200*ms)

    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Binary value')

def recipe_d1b():
    with DigitalIn(line=0, rate=50*kHz) as di:
        data, times = di.read(200*ms, times=True)

    plt.plot(times, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Binary value')


def recipe_d2a():
    with DigitalIn(lines=[0, 1], rate=50*kHz) as di:
        data = di.read(200*ms)

    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Binary value')

    
def recipe_d2raw():
    import numpy as np
    
    with DigitalIn(lines=[0, 1], rate=50*kHz) as di:
        data = di.read(200*ms, raw=True)

    bits = np.unpackbits(data, bitorder='little').reshape(-1, 8).T
    plt.imshow(bits[:,:200], aspect='auto', interpolation='none')
    plt.xlabel('Byte #')
    plt.ylabel('Bit #')
    
showall(vars())
    
