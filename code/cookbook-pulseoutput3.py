#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the increasing-count examples 

from picodaq import *
from picodaq.stimulus import Pulse, Train, Series, Deltas
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall

pulse = Pulse(amplitude=1*V, duration=50*ms)
pudelta = Deltas(amplitude=0.2*V)
trdelta = Deltas(pulsecount=1, duration=-10*ms)
train = Train(pulse, pulseperiod=200*ms, pulsecount=2,
              perpulse=pudelta)
series = Series(train, trainperiod=1*s, traincount=3,
                pertrain=trdelta)

def recipe_po3a():
    ##importall
    from picodaq.stimulus import Pulse, Train, Series, Deltas

    pulse = Pulse(amplitude=1*V, duration=50*ms)
    pudelta = Deltas(amplitude=0.2*V)
    trdelta = Deltas(pulsecount=1, duration=-10*ms)
    train = Train(pulse, pulseperiod=200*ms, pulsecount=2,
                  perpulse=pudelta)
    series = Series(train, trainperiod=1*s, traincount=3,
                    pertrain=trdelta)
    with AnalogOut(rate=50*kHz) as ao:
        ao[0].stimulus(train)
        ao.run()

        
def recipe_po3b():
    import matplotlib.pyplot as plt
    from picodaq.mockstim import mockstim
   
    plandata = mockstim(series, rate=50*kHz)
    plt.plot(plandata)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')

   
showall(vars())
    
