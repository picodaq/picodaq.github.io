#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the TTL pulse examples 

from picodaq import *
from picodaq.stimulus import TTL, Train
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall

pulse = TTL(duration=50*ms)
train = Train(pulse, pulseperiod=200*ms, pulsecount=10)


def recipe_po5a():
    ##importall
    from picodaq.stimulus import TTL, Train

    pulse = TTL(duration=50*ms)
    train = Train(pulse, pulseperiod=200*ms, pulsecount=10)
    with DigitalOut(rate=50*kHz) as do:
        do[0].stimulus(train)
        do.run()

        
def recipe_po5b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata = mockstim(train, rate=50*kHz)
    plt.plot(plandata)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (logic)')
    plt.yticks([0,1])

    
def recipe_po5c():
    with DigitalOut(rate=50*kHz) as do:
        with DigitalIn(line=0) as di:
            do[0].stimulus(train)
            data, times = di.read(2*s, times=True)

    plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
    plt.xlabel('Time (s)')
    plt.ylabel('Input (logic)')
    plt.yticks([0,1])
    
    
showall(vars())
    
