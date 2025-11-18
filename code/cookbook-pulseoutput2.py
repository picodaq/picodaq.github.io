#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the asymmetric biphasic examples 

from picodaq import *
from picodaq.stimulus import Square, Train
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall

pulse = Square(amplitude=5*V, duration=100*ms,
               amplitude2=-2.5*V, duration2=200*ms)
train = Train(pulse, pulseperiod=500*ms, pulsecount=4)


def recipe_po2a():
    ##importall
    from picodaq.stimulus import Square, Train

    pulse = Square(amplitude=5*V, duration=100*ms,
                   amplitude2=-2.5*V, duration2=200*ms)
    train = Train(pulse, pulseperiod=500*ms, pulsecount=4)
    with AnalogOut(rate=50*kHz) as ao:
        ao[0].stimulus(train)
        ao.run()

        
def recipe_po2b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata = mockstim(train, rate=50*kHz)
    plt.plot(plandata)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')

    
def recipe_po2c():
    with AnalogOut(rate=50*kHz) as ao:
        with AnalogIn(channel=0) as ai:
            ao[0].stimulus(train)
            ao.run()
            data, times = ai.readall(times=True)

    plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    
    
showall(vars())
    
