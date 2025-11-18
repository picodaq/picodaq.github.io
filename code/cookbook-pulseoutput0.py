#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the basic pulse examples 

from picodaq import *
from picodaq.stimulus import Pulse, Train
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall

pulse = Pulse(amplitude=1*V, duration=50*ms)
train = Train(pulse, pulseperiod=200*ms, pulsecount=10)


def recipe_po0a():
    ##importall
    from picodaq.stimulus import Pulse, Train

    pulse = Pulse(amplitude=1*V, duration=50*ms)
    train = Train(pulse, pulseperiod=200*ms, pulsecount=10)
    with AnalogOut(rate=50*kHz) as ao:
        ao[0].stimulus(train)
        ao.run()

        
def recipe_po0b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata = mockstim(train, rate=50*kHz)
    plt.plot(plandata)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')

    
def recipe_po0c():
    with AnalogOut(rate=50*kHz) as ao:
        with AnalogIn(channel=0) as ai:
            ao[0].stimulus(train)
            data, times = ai.read(2*s, times=True)

    plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    
    
showall(vars())
    
