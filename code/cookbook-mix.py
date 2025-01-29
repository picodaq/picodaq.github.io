#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

from picodaq import *
import matplotlib.pyplot as plt
from code.cookbookhelper import showall


def recipe_mix1a():
    ##importall
    import matplotlib.pyplot as plt

    with AnalogIn(channel=0, rate=50*kHz) as ai:
        with DigitalIn(line=0, rate=50*kHz) as di:
            adata = ai.read(200*ms)
            ddata = di.read(200*ms)

    plt.plot(adata)
    plt.plot(ddata)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V) / Binary value')

def recipe_mix1b():
    import numpy as np

    adata = []
    ddata = []
    K = 10
    with AnalogIn(channel=0, rate=50*kHz) as ai:
        with DigitalIn(line=0, rate=50*kHz) as di:
            for k in range(K):
                adata.append(ai.read(50*ms))
                ddata.append(di.read(50*ms))
    adata = np.concatenate(adata, 0)
    ddata = np.concatenate(ddata, 0)
    
    plt.plot(adata)
    plt.plot(ddata)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V) / Binary value')


showall(vars())
    
