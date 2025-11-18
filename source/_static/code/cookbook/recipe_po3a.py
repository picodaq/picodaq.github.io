from picodaq import *
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
