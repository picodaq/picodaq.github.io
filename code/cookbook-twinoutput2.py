#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the basic pulse examples 

from picodaq import *
from picodaq.stimulus import TTL, Train
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall

pulse1 = TTL(duration=100*ms)
train1 = Train(pulse1, pulseperiod=200*ms, pulsecount=5)
pulse2 = TTL(duration=30*ms)
train2 = Train(pulse2, pulseperiod=100*ms, pulsecount=10)


def recipe_to2a():
    ##importall
    from picodaq.stimulus import TTL, Train

    pulse1 = TTL(duration=100*ms)
    train1 = Train(pulse1, pulseperiod=200*ms, pulsecount=5)
    pulse2 = TTL(duration=30*ms)
    train2 = Train(pulse2, pulseperiod=100*ms, pulsecount=10)

    with DigitalOut(rate=50*kHz) as do:
        do[0].stimulus(train1)
        do[1].stimulus(train2, delay=20*ms)
        do.run()

        
def recipe_to2b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata1 = mockstim(train1, rate=50*kHz)
    plandata2 = mockstim(train2, rate=50*kHz, delay=20*ms)
    plt.plot(plandata1 + 2)
    plt.plot(plandata2)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (logic)')
    plt.yticks([0, 1, 2, 3], [0, 1, 0, 1])    

    
def recipe_to2c():
    with DigitalOut(rate=50*kHz) as do:
        with DigitalIn(lines=[0, 1]) as di:
            do[0].stimulus(train1)
            do[1].stimulus(train2, delay=20*ms)
            do.run()
            data, times = di.readall(times=True)
    
    plt.plot(times, data[:,0] + 2)
    plt.plot(times, data[:,1])
    plt.xlabel('Time (s)')
    plt.ylabel('Input (logic)')
    plt.yticks([0, 1, 2, 3], [0, 1, 0, 1])
    
showall(vars())
    
