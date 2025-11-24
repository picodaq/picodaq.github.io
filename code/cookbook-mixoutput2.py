from scipy.signal import sweep_poly
import numpy as np
from cookbookhelper import showall
from picodaq import *
from picodaq.stimulus import TTL, Train
import matplotlib.pyplot as plt
from picodaq.mockstim import mockstim, mock

f0 = 10 * Hz
f1 = 100 * Hz
dur = 1 * s
fs = 10 * kHz

tt_s = np.arange(0, dur.as_('s'), (1/fs).as_('s'))
poly = [(f1-f0).as_('Hz') / dur.as_('s'), f0.as_('Hz')]
vv = sweep_poly(tt_s, poly, phi=-90)

pulse = TTL(duration=20*ms)
train = Train(pulse, pulseperiod=100*ms, pulsecount=10)


def recipe_mo2a():
    ##importall
    from scipy.signal import sweep_poly
    import matplotlib.pyplot as plt
    import numpy as np
    
    f0 = 10 * Hz
    f1 = 100 * Hz
    dur = 1 * s
    fs = 10 * kHz
    
    tt_s = np.arange(0, dur.as_('s'), (1/fs).as_('s'))
    poly = [(f1-f0).as_('Hz') / dur.as_('s'), f0.as_('Hz')]
    vv = sweep_poly(tt_s, poly, phi=-90)

    pulse = TTL(duration=20*ms)
    train = Train(pulse, pulseperiod=100*ms, pulsecount=10)

    
def recipe_mo2c():
    with AnalogOut(rate=fs) as ao:
        with DigitalOut() as do:
            with AnalogIn(channel=0) as ai:
                with DigitalIn(line=0) as di:
                    ao[0].sampled(vv, scale=1*V)
                    do[0].stimulus(train)
                    ao.run()
                    data, times = ai.readall(times=True)
                    ddata = di.readall()

    plt.plot(times, data, '.-', markersize=1, linewidth=0.1)
    plt.plot(times, -1.5 + .3*ddata)
    plt.xlabel('Time (s)')
    plt.ylabel('Logic input / Voltage (V)')
    plt.yticks([-1.5, -1.2, -1, 0, 1], ['Lo', 'Hi', -1, 0, 1])

    
showall(vars())
