.. _installation:

Requirements
............................

The Exo-Striker runs on **Linux**, **macOS** and **Windows** (10/11).

1. **Python 3.10 or newer** is required. Use a separate environment (see below) instead of replacing your system Python.

2. Some parts of the tool are compiled on your computer, so you also need:

* gcc (a C compiler)
* gfortran
* csh
* the Python development headers (on Linux usually a package named like ``python3.10-dev``), in case the Exo-Striker does not want to compile.

3. All Python dependencies (numpy, scipy, PyQt6, rebound, batman, celerite, wotan, ttvfast, etc.) are installed **automatically** by ``pip``. The full list is in the ``pyproject.toml`` file of the `source repository <https://github.com/3fon3fonov/exostriker>`_.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Prepare an environment (recommended)
......................................

**Option A: virtual environment (without Anaconda)**

.. code-block:: bash

   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip

On Windows, use ``py -m venv .venv`` and activate it with ``.venv\Scripts\activate`` in CMD, or ``.venv\Scripts\Activate.ps1`` in PowerShell.

**Option B: Anaconda** (recommended especially for Windows users)

1. Download and install `Anaconda <https://www.anaconda.com/products/individual#download-section>`_.
2. Create and activate an environment for the Exo-Striker:

.. code-block:: bash

   conda create -n exostriker python=3.10
   conda activate exostriker

3. On Windows (and on some newer Apple M-chip Macs) Anaconda may not find GFortran. Install it inside the activated environment:

.. code-block:: bash

   conda install conda-forge::gfortran

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Installation
............................

There are **three ways to install/run** the Exo-Striker. They work on Linux, Windows and macOS, as long as Python and GFortran are installed.

* The **first way (recommended)** is to install the version from **PyPI**:

.. code-block:: bash

   pip install exostriker

or, for a specific Python version, e.g.:

.. code-block:: bash

   python3.10 -m pip install exostriker

**This is all.**

-------------------------------------------------------------------------

* The **second way** is to install from the **source** code on GitHub:

.. code-block:: bash

   git clone https://github.com/3fon3fonov/exostriker.git
   cd exostriker
   python -m pip install .

For development, use ``python -m pip install -e .`` instead.

-------------------------------------------------------------------------

* The **third way** is to **run without installation**. Install the required dependencies in your active environment first, then:

.. code-block:: bash

   git clone https://github.com/3fon3fonov/exostriker.git
   cd exostriker
   python3 -m exostriker

Launch it from the repository root with ``python -m exostriker``; running ``gui.py`` directly bypasses the package entry point.

.. note::
	When starting for the first time, the Fortran parts of the tool are compiled, and an update may trigger recompilation. The first start can take longer, so keep GFortran and the build tools installed.

**Optional: integrated AI chat**

The Exo-Striker includes an optional AI chat. To install it:

.. code-block:: bash

   python -m pip install "exostriker[chat]"

or ``python -m pip install ".[chat]"`` from the source folder. An **OpenAI API key** is required to use the chat.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting the GUI
............................

After installation, start the Exo-Striker with:

.. code-block:: bash

   exostriker

or

.. code-block:: bash

   python -m exostriker

To create menu entries (and, on Windows, a Desktop link):

.. code-block:: bash

   exostriker-desktop-create

Then search for *Exostriker* in your menu.

**Working directory and settings**

The ``exostriker`` launcher uses your **home directory** as its working directory on Linux, macOS and Windows. Settings are saved in ``~/.exostriker/ES_settings.json``, created from the default settings on first use.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Updating and checking the version
....................................

To update a pip installation:

.. code-block:: bash

   python -m pip install --upgrade exostriker

If you installed from source, run ``git pull`` in the ``exostriker`` folder and install again with ``python -m pip install .``. Restart the Exo-Striker after updating.

To check the installed version without starting the GUI:

.. code-block:: bash

   python -c "from importlib.metadata import version; print(version('exostriker'))"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Adding pip scripts to the PATH (without Anaconda)
....................................................

If you do not use Anaconda and the ``exostriker`` command is not found, add the folder of the pip scripts to your system path. **This step is not necessary if you run without installation.**

**Linux:** add this line at the end of ``~/.bashrc`` (change ``USER`` to your user name):

.. code-block:: bash

   export PATH="${PATH}:/home/USER/.local/bin/"

The location can differ between Linux distributions and Python installations. If this does not work, try other paths such as ``/usr/local/bin``.

**Windows:** open the menu and search for *path*, click *Edit the system environment variables*, then *Environment Variables...*. In *System variables* (not *User variables*), select *Path*, click *Edit* and add the ``Scripts`` folder of your Python installation, for example:

``C:\Users\USERNAME\AppData\Local\Programs\Python\Python311\Scripts``

The path changes with the Python version, so always check that it exists.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Windows 10&11 step by step (without Anaconda)
...............................................

1. **Python:** download a stable 64-bit Windows installer from `Python Windows Releases <https://www.python.org/downloads/windows/>`_ and install it. Add these two folders to the *Path* (as above), changing ``USERNAME`` and ``Python311`` to your values:

	``C:\Users\USERNAME\AppData\Local\Programs\Python\Python311``

	``C:\Users\USERNAME\AppData\Local\Programs\Python\Python311\Scripts``

   In the Python folder, make a copy of ``python.exe`` in the same place and name it ``python3.11.exe``.

2. **GFortran:** download the *x64* version of `WinLibs <https://winlibs.com>`_ (x64 POSIX **with** all the libraries). Unpack it, move the ``mingw64`` folder to ``C:\Program Files\`` and add ``C:\Program Files\mingw64\bin`` to the *Path*.

3. **Microsoft C++ Build Tools** (needed for the TTVFast package): download the `Build Tools <https://visualstudio.microsoft.com/visual-cpp-build-tools/>`_ and, during installation, select *Desktop development with C++*.

4. **Exo-Striker:** in CMD type:

.. code-block:: bash

   pip install exostriker

If native compilation fails, check that the compiler and build tools are visible in the same terminal/environment you use to start the Exo-Striker, and read the reported compiler error.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Uninstall
............................

If you run the tool without installation, just delete the ``exostriker`` folder. Otherwise, first remove the menu entries (if you created them), then uninstall:

.. code-block:: bash

   exostriker-desktop-remove
   pip uninstall exostriker

------------------------------------------------------------------------------------------------------------

Common issues and solutions
....................................

If the GUI does not start after a successful installation, please try:

``exostriker -debug``  (or ``python -m exostriker -debug``)

This command starts the GUI and at the same time outputs an error message with few guidelines, which are otherwise displayed in the 'stdout/stderr' tab of the GUI.

1. Broken appearance of GUI under Windows (WSL / X-server)

.. todo:: This tip is for running the Exo-Striker through WSL and an X-server (the old Windows method). Check with the developer whether it is still needed now that native Windows installation works.


In case there is a problem of the appearance of the GUI the problem could be 
your DPI setup. On high DPI displays with Windows display scaling activated (>100%), the X-server DPI has to be set, otherwise, the Exo-Striker will not display correctly (text clipping).
Edit the file `.Xresources` in the home directory of the WSL installation, for example with `nano ~/.Xresources`.
Add the line `Xft.dpi: 100` and save & close with Ctrl+O Ctrl+X, then reload the X configuration with `xrdb ~/.Xresources`.
On Ubuntu WSL you might need to install `x11-xserver-utils` with `sudo apt install x11-xserver-utils` for xrdb to be available.

Launch the Exo-Striker and check the scaling. If text is clipping, the DPI needs to be set lower, if everything is too small, the DPI needs to be higher. Remember always to reload the configuration with `xrdb ~/.Xresources`. For the configuration to automatically load at startup, add the xrdb command to your ~/.bashrc, after the `export DISPLAY=:0.0`.

2. Broken appearance of GUI under Linux


A computer display with low resolution may not properly display the interface of Exo-Striker (text clipping, missing plot parts, missing buttons).
There is a workaround using Xrandr.

``xrandr -q``

The  command will output current monitor and available resolutions. 

Set the necessary parameters, for example:

``xrandr --output eDP-1 --mode 1366x768 --scale 1.20x1.20 --panning 1920x1080``

Here eDP-1 is the current monitor, mode is the current resolution, scale is the scale factor for desired resolution, panning is the whole area available with scrolling after the new resolution is set. If panning is not used, the whole screen fits in the display window.

More issues and more thorough explanations and solutions are available in the *Issues section* of the `GitHub repository`_.

----------------------------------------------------------------------------------------------------------------------------

Report an issue
..................

If you run into issues or bugs, do not hesitate to report a **New issue** on the `GitHub repository`_ or send a PM to trifonov@mpia.de.

.. _GitHub repository: https://github.com/3fon3fonov/exostriker/issues 

**Feedback** and **help** in further development will be highly appreciated! A wish-list with your favorite tools and methods to be implemented is also welcome!


