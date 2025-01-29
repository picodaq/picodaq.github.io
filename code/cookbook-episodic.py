#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

from picodaq import *
import matplotlib.pyplot as plt
from code.cookbookhelper import showall


def recipe_epi1a():
    ##importall
    import matplotlib.pyplot as plt
    import numpy as np

    data = []
    K = 20
    with AnalogIn(channel=0, rate=100*kHz) as ai:
        ai.episodic(duration=20*ms, period=100*ms)
        for k in range(K):
            data.append(ai.read())
    data = np.stack(data, 1)
                        
    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')

showall(vars())
    
