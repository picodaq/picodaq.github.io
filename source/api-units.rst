.. _api-units:

Units for time, frequency, and voltage
======================================

picoDAQ defines the classes ``Time``, ``Frequency``, and ``Voltage``
to represent times, frequencies and voltages.

Generally, you do not contruct instances of these classes directly,
but use the constants ``s``, ``ms``, ``Hz``, ``kHz``, ``V``, ``mV``
that represent, respectively, one second, one millisecond, one hertz,
one kilohertz, one volt, and one millivolt.

For instance, to specify a pulse with amplitude 2.5 volt, you might write ``amplitude = 2.5*V``.

Arithmetic is fully supported.  For instance, ``3*s/2 + 3.5*100*ms`` is
a valid way to represent 1.85 seconds.

The system also knows that time and frequency are each other
reciprocal. Thus, ``10000/s`` and ``10*kHz`` are both valid ways to
represent 10 kilohertz.

To convert the unitless product of a time and a frequency back to a
plain number, use the `plain()` method, as in::

    duration = 10 * s
    rate = 5 * Hz
    pulsecount = int((duration * rate).plain())

(Without the explicit `int` cast, the result would be float.)


Implementation details
----------------------

Time, Frequency and Voltage are implemented as derived classes from a
general :ref:`Quantity <api-quantity>` class. Most users do not need to use that class directly.

.. toctree::
   :maxdepth: 3
   :titlesonly:
   :hidden:

   api-quantity
   
