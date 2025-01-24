.. _installation:

Installation
============


All you need to get started with picoDAQ is a single Python library,
called `picodaq`. There are no hardware drivers to install.

The latest version of the library is always
available through the python package archive and may be installed as follows.

Command line
------------

In Windows, Mac OS, and many versions of Linux, a simple

    pip install picodaq

gets you the latest. This works without restriction in `virtual
environments <https://docs.python.org/3/library/venv.html>`_ as well.

IDEs
----
    
Many Python IDEs provide convenient front ends for ``pip``. For instance, in PyCharm...
In VSCode ...


Verifying software installation
-------------------------------

Open your favorite Python IDE. Type

    import picodaq
    print(picodaq.version)
    
Run that code. You should be greeted with a version number, like

    "0.1.240124"

If, instead, you receive a ModuleNotFoundError exception, check your
typing and make sure that the environment used by your IDE includes
the place where you installed the ``picodaq`` library. It may be helpful to

    import sys
    print(sys.path)
    
Troubleshooting strategies for this situation vary by
IDE. Fortunately, advice is broadly available on the internet.

Next steps
----------

Now that you have installed picoDAQ, the next step is to :ref:`see if it works <firstrun>`.
