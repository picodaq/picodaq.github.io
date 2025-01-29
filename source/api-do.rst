.. _api-do:

DigitalOut
==========

.. autoclass:: picodaq.dac.DigitalOut
   :members:
   :inherited-members:
   :special-members: __getitem__

Specifying stimuli
------------------

To specify stimuli for a given output channel, use indexing syntax on
a `DigitalOut` object (i.e., something like ``do[1]``), then use the
`stimulus()` or `sampled()` methods on the returned `OutRef`
object. See also :ref:`funcoutput1` and :ref:`sampleout` in the
:ref:`Cookbook <cookbook>` section of the picoDAQ documentation.

Note that the `OutRef` class is used for both analog and digital
stimuli. When used for digital stimuli, only a subset of the
parameters to `stimulus()` and `sampled()` are used, as documented
below.

     
.. autoclass:: picodaq.dac.OutRef
   :members:
   :no-index:    
  
