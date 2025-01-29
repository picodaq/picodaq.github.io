#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

from picodaq import *
import matplotlib.pyplot as plt
from code.cookbookhelper import showall


def recipe_a2a():
    ##importall
    import matplotlib.pyplot as plt

    with AnalogIn(channels=[0, 1], rate=50*kHz) as ai:
        data = ai.read(200*ms)

    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')

    
def recipe_a2b():
    ##importall
    import matplotlib.pyplot as plt

    with AnalogIn(channels=[0, 1], rate=50*kHz) as ai:
        data, times = ai.read(200*ms, times=True)

    plt.plot(times, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')

    

showall(vars())
    
