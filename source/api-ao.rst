.. _api-ao:

AnalogOut
=========

.. autoclass:: picodaq.dac.AnalogOut
   :members:
   :inherited-members:
   :special-members: __getitem__

                     
Specifying stimuli
------------------

To specify stimuli for a given output channel, use indexing syntax on
an `AnalogOut` object (i.e., something like ``ao[1]``), then use the
`stimulus()` or `samples()` methods on the returned `OutRef`
object. See also :ref:`funcoutput1` and :ref:`sampleout` in the :ref:`Cookbook
<cookbook>` section of the picoDAQ documentation.


.. autoclass:: picodaq.dac.OutRef
   :members:
