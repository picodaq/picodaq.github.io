import numpy as np
from code.cookbookhelper import showall
from picodaq import *
from picodaq.stimulus import Triangle, TTL, Train
import matplotlib.pyplot as plt
from picodaq.mockstim import mockstim

fs = 10 * kHz
apulse = Triangle(duration=50*ms, amplitude=1*V)
atrain = Train(apulse, pulseperiod=100*ms, pulsecount=9)
dpulse = TTL(duration=20*ms)
dtrain = Train(dpulse, pulseperiod=200*ms, pulsecount=5)


def recipe_mo1a():
    ##importall
    from picodaq.stimulus import Triangle, TTL, Train
    import matplotlib.pyplot as plt
    import numpy as np

    fs = 10 * kHz
    apulse = Triangle(duration=50*ms, amplitude=1*V)
    atrain = Train(apulse, pulseperiod=100*ms, pulsecount=9)
    dpulse = TTL(duration=20*ms)
    dtrain = Train(dpulse, pulseperiod=200*ms, pulsecount=5)

    aplandata, att = mockstim(atrain, rate=fs, times=True)
    dplandata, dtt = mockstim(dtrain, rate=fs, times=True)

    plt.plot(att, aplandata)
    plt.plot(dtt, -1.5 + .3*dplandata)
    plt.xlabel('Time (s)')
    plt.ylabel('Planned logic / voltage (V)')
    plt.yticks([-1.5, -1.2, -1, 0, 1], ['Lo', 'Hi', -1, 0, 1])

    
def recipe_mo1c():
    with AnalogOut(rate=fs) as ao:
        with DigitalOut() as do:
            with AnalogIn(channel=0) as ai:
                with DigitalIn(line=0) as di:
                    ao[0].stimulus(atrain)
                    do[0].stimulus(dtrain)
                    ao.run()
                    adata, times = ai.readall(times=True)
                    ddata = di.readall()

    plt.plot(times, adata, '.-', markersize=1, linewidth=0.1)
    plt.plot(times, -1.5 + .3*ddata)
    plt.xlabel('Time (s)')
    plt.ylabel('Logic input / Voltage (V)')
    plt.yticks([-1.5, -1.2, -1, 0, 1], ['Lo', 'Hi', -1, 0, 1])

    
showall(vars())
