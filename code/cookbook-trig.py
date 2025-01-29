#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

from picodaq import *
import matplotlib.pyplot as plt
from code.cookbookhelper import showall


def recipe_trig1a():
    ##importall
    import matplotlib.pyplot as plt
    
    with AnalogIn(channel=0, rate=100*kHz) as ai:
        with DigitalIn(line=0) as di:
            ai.trigger(0, polarity=1)
            data = ai.read(100*ms)
            ddata = di.read(100*ms)
                        
    plt.plot(data)
    plt.plot(ddata)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')

    
def recipe_trig1b():
    ##importall
    import matplotlib.pyplot as plt
    
    with AnalogIn(channel=0, rate=100*kHz) as ai:
        ai.trigger(0, polarity=-1)
        data = ai.read(100*ms)
                        
    plt.plot(data)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')
    
   
def recipe_trig1c():
    import numpy as np

    data = []
    ddata = []
    K = 20
    with AnalogIn(channel=0, rate=100*kHz) as ai:
        with DigitalIn(line=0) as di:
            ai.episodic(duration=19*ms, period=0*ms)
            ai.trigger(0, polarity=1)
            for k in range(K):
                data.append(ai.read())
                ddata.append(di.read())
    data = np.stack(data, 1)
    ddata = np.stack(ddata, 1)
                        
    plt.plot(data)
    plt.plot(ddata)
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')

showall(vars())
    
