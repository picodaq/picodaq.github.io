.. _hwspecs:

Hardware Specifications
=======================

Analog input
------------

.. rst-class:: spec-table
.. list-table::
   :widths: 40 20 20
   :header-rows: 1
   :stub-columns: 1                

   * -
     - picoDAQ lite
     - picoDAQ pro
   * - Number of channels
     - 2
     - 4
   * - Voltage range
     - ±10 V
     - ±10 V
   * - Bit depth
     - 12 bits
     - 16 bits
   * - Max. sampling rate
     - xxx kHz²⁾
     - xxx kHz³⁾
   * - Max. sustained throughput
     - xxx kS/s
     - xxx kS/s
   * - Broadband noise
     - xxx mV¹⁾
     - yyy mV¹⁾

      
Notes
~~~~~

1. RMS, measured over 10 Hz to 10 kHz
2. For one channel.  Two channels are sampled sequentially, each at
   half the max. rate.
3. All channels simultaneous
       
       
Analog output
-------------

.. rst-class:: spec-table
.. list-table::
   :widths: 40 20 20
   :header-rows: 1
   :stub-columns: 1                

   * -
     - picoDAQ lite
     - picoDAQ pro
   * - Number of channels
     - 2
     - 4
   * - Voltage range
     - ±10 V
     - ±10 V
   * - Bit depth
     - 10/12 bits¹⁾
     - 16 bits
   * - Max. sampling rate
     - xxx kHz²⁾
     - xxx kHz³⁾
   * - Noise
     - xxx mV¹⁾
     - yyy mV¹⁾

       
Notes
~~~~~

1. At 100 kHz/10 kHz. The picoDAQ lite uses PWM for generating analog
   outputs. The effective bit depth therefore is reduced at higher
   sampling rates.

       
Digital input
-------------

.. rst-class:: spec-table
.. list-table::
   :widths: 40 20 20
   :header-rows: 1
   :stub-columns: 1                

   * -
     - picoDAQ lite
     - picoDAQ pro
   * - Number of lines
     - 2
     - 4

       
Digital output
--------------

.. rst-class:: spec-table
.. list-table::
   :widths: 40 20 20
   :header-rows: 1
   :stub-columns: 1                

   * -
     - picoDAQ lite
     - picoDAQ pro
   * - Number of lines
     - 2
     - 4
 
