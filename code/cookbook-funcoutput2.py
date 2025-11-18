#!/usr/bin/python3

# There is not a build system that builds the cookbook images
# automatically, as cloud services tend not to have picoDAQs
# attached to their VMs yet.

# These are the sinewave examples

import numpy as np
from picodaq import *
from picodaq.stimulus import Wave, Train
from picodaq.mockstim import mockstim, mock
import matplotlib.pyplot as plt
from code.cookbookhelper import showall

f_out = 50*kHz
f_wave = 5*Hz
sinedata = np.sin(np.linspace(0, 2*np.pi,
                              int((f_out/f_wave).plain()), endpoint=False))
pulse = Wave(data=sinedata, scale=8*V)
train = Train(pulse, pulseperiod=1/f_wave, pulsecount=10)


def recipe_fo2a():
    ##importall
    import numpy as np

    f_out = 50*kHz
    f_wave = 5*Hz
    samples_per_period = int((f_out/f_wave).plain())

    sinedata = np.sin(np.linspace(0, 2*np.pi, samples_per_period,
                                  endpoint=False))

        
def recipe_fo2b():
    import matplotlib.pyplot as plt
    from picodaq.stimulus import Wave, Train
    from picodaq.mockstim import mockstim
   
    pulse = Wave(data=sinedata, scale=8*V)
    train = Train(pulse, pulseperiod=1/f_wave, pulsecount=10)
    plandata = mockstim(train, rate=50*kHz)
    plt.plot(plandata)
    plt.xlabel('Sample #')
    plt.ylabel('Planned output (V)')

    
def recipe_fo2c():
    with AnalogOut(rate=50*kHz) as ao:
        with AnalogIn(channel=0) as ai:
            ao[0].stimulus(train)
            ao.run()
            data, times = ai.readall(times=True)

    plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    
    
showall(vars())
    
