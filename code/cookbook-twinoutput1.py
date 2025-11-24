#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the basic pulse examples 

from picodaq import *
from picodaq.stimulus import Square, Triangle, Train
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall

pulse1 = Triangle(amplitude=0.7*V, duration=100*ms)
train1 = Train(pulse1, pulseperiod=200*ms, pulsecount=5)
pulse2 = Square(amplitude=0.5*V, duration=30*ms)
train2 = Train(pulse2, pulseperiod=100*ms, pulsecount=10)


def recipe_to1a():
    ##importall
    from picodaq.stimulus import Square, Triangle, Train

    pulse1 = Triangle(amplitude=0.7*V, duration=100*ms)
    train1 = Train(pulse1, pulseperiod=200*ms, pulsecount=10)
    pulse2 = Square(amplitude=1*V, duration=25*ms)
    train2 = Train(pulse2, pulseperiod=100*ms, pulsecount=20)
    with AnalogOut(rate=50*kHz) as ao:
        ao[0].stimulus(train1)
        ao[1].stimulus(train2)
        ao.run()

        
def recipe_to1b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata1 = mockstim(train1, rate=50*kHz)
    plandata2 = mockstim(train2, rate=50*kHz)
    plt.plot(plandata1)
    plt.plot(plandata2)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')

    
def recipe_to1c():
    with AnalogOut(rate=50*kHz) as ao:
        with AnalogIn(channels=[0, 1]) as ai:
            ao[0].stimulus(train1)
            ao[1].stimulus(train2)
            ao.run()
            data, times = ai.readall(times=True)

    plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    
    
showall(vars())
    
