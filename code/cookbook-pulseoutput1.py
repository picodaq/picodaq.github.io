#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the increasing-amplitude examples 

from picodaq import *
from picodaq.stimulus import Pulse, Train, Deltas
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall
pulse = Pulse(amplitude=1*V, duration=50*ms)
delta = Deltas(amplitude=0.2*V)
train = Train(pulse, pulseperiod=200*ms, pulsecount=10, perpulse=delta)


def recipe_po1a():
    ##importall
    from picodaq.stimulus import Pulse, Train, Deltas

    pulse = Pulse(amplitude=1*V, duration=50*ms)
    delta = Deltas(amplitude=0.2*V)
    train = Train(pulse, pulseperiod=200*ms, pulsecount=10,
                  perpulse=delta)
    with AnalogOut(rate=50*kHz) as ao:
        ao[0].stimulus(train)
        ao.run()

        
def recipe_po1b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata = mockstim(train, rate=50*kHz)
    plt.plot(plandata)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')

   
showall(vars())
    
