#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

from picodaq import *
from picodaq.stimuli import Square, Train
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall
pulse = Pulse(amplitude=1*V, duration=10*ms)
train = Train(pulse, trainperiod=20*ms, pulsecount=100)


def recipe_fo1a():
    ##importall
    from picodaq.stimuli import Square, Train

    pulse = Pulse(amplitude=1*V, duration=10*ms)
    train = Train(pulse, trainperiod=20*ms, pulsecount=100)
    with AnalogOut(channel=0, rate=50*kHz) as ao:
        ao[0].stimulus(train)
        ao.run()

        
def recipe_fo1b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata = mockstim(train, rate=50*kHz)
    plt.plot(plandata)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')

    
def recipe_fo1c():
    with AnalogOut(channel=0, rate=50*kHz) as ao:
        with AnalogIn() as ai:
            ao[0].stimulus(train)
            ao.run()
            data, times = ai.readall(times=True)

    plt.plot(times, data)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    
    
showall(vars())
    
