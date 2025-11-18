from picodaq import *
import numpy as np

f_out = 50*kHz
f_wave = 5*Hz
samples_per_period = int((f_out/f_wave).plain())

sinedata = np.sin(np.linspace(0, 2*np.pi, samples_per_period,
                              endpoint=False))
