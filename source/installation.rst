.. _installation:

Linux
............................

Prerequisites

1. To **install** the Exo-Striker, first please make sure that you have installed the following packages:

* csh
* gfortran
* pip


2. Use **Python 3** for installing the Exo-Striker! The tool works with Python 2; however as of Jan 1, 2020, Python 2 is no longer being maintained and eventual problems may not be addressed.


3. Do not uninstall the Python version which was default to your system, this may cause unexpected side effects. If you have an older version of Python, keep it and install the newer one as well. 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Currently there are **three ways to install/run** the Exo-Striker:
   
* The **first way** is to **git clone** using the Linux command line:
 
``git clone https://github.com/3fon3fonov/exostriker``  

``cd exostriker``

and then **load the GUI**:    

``python3 exostriker_gui.py``

**or** 

``./exostriker_gui.py``

This installation process clones the repository in a local folder and installs the tool locally.

To update the tool:

``git pull``

-------------------------------------------------------------------------

* The **second way** to install the tool from the source:    

``git clone https://github.com/3fon3fonov/exostriker``

and then:    

``cd exostriker``

``python3 setup.py install``

This command will initiate a global installation on your system.   
  
Then,      

``python3 exostriker_gui.py``

This should start the Exo-Striker GUI  

----------------------------------------------------------------

* and **third way** is to **pip3 install**:    

``pip3 install git+https://github.com/3fon3fonov/exostriker``

This command will initiate a global installation on your system.  
   
Then,     

``python3 exostriker_gui.py``

**or** 

``exostriker``

This should start the Exo-Striker GUI.


In order to update the tool, when a new version is available, the syntax is:

pip3 install git+https://github.com/3fon3fonov/exostriker -U

.. note::
	When installing and running for the first time, some additional libraries are being decompiled and it takes several minutes more to start the GUI.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Generally, **you do not need to install anything if you already have all the required dependencies** for the tool to run.
The dependency list, including the version of each dependency, can also be seen at the "setup.py" file.

.. IMPORTANT::
   List of required **dependencies** : 

    * numpy
    * scipy
    * matplotlib
    * PyQt5
    * jupyter
    * pathos
    * emcee  
    * celerite
    * qtconsole
    * dynesty
    * wotan 
    * corner
    * transitleastsquares
    * ttvfast-python
    
In some occasions it will be necessary to manually install packages/modules such as tqdm, wotan, batman, etc, which usually depends on the Linux distribution and Python version.

To do so use pip3, eg.

``pip3 install tqdm``

For more details visit `Common issues and solutions`_.


.. tip::	
	* Install the simple and extensible rxvt terminal emulator:

	See rxvt documentation here: https://wiki.archlinux.org/title/rxvt-unicode

	* Install Anaconda package which manages the dependencies and may resolve installation issues.

	See Anaconda documentation here: https://docs.anaconda.com/anaconda/install/.
	
-----------------------------------------------------------------------------------------------------

Windows 10&11
...................

Prerequisites:

1. **Windows subsystem for Windows - WSL & WSL2**

	Installation on Windows 10 and 11 works only troughs the "Windows Subsystem for Linux".
	
	Please follow this guide:
	
	`Install WSL <https://docs.microsoft.com/en-us/windows/wsl/install>`_

	
	Follow all the steps carefully! This way you will be able to run all Linux native programs on your WINDOWS 10 & 11 bash shell, which is very useful in general!

	Please install the Ubuntu 20.04 LTS !!!
	
2. **XServer**

	To make The Exo-Striker work, however, you also will need an XServer installed.
	
	Follow these instructions carefully:

	`Install XServer <https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/>`_
	
3. **Update the Linux kernel**

	After installing Ubuntu 20.04 LTS app on your Windows OS, open the app and update the Linux kernel:

	``sudo apt update``
	
	``sudo apt dist-upgrade -y``
	
	When done, write the following lines in the Linux Terminal:

	``sudo apt install build-essential curl git gfortran gcc+ csh xterm``
	
	
4. **Fix the Qt libraries**

	For some unknown reason, some qt binaries in Ubuntu 20.04+ are missing. Just in case, run all these commands:
	
	``sudo apt install libxcb-xinerama0``
	
	``sudo apt install libxkbcommon-x11-0``
	
	``sudo apt install qt5-default``
	
5. **Python3.8 and pip3.8**
	
	Python 3.8+ is strongly recommended!!! On your WSL on Windows and Ubuntu 20.04, you will likely have Python 3.8.2 installed, but to install the newest Python 3.8.13 (or later) alongside your system Python 3.8.2, you can try these instructions (for 18.04 but should be OK for 20.04):
	
	`Install Python <https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/>`_
	
	Let's assume, you now have Python3.8, then it is recommended to install pip3.8:
		
	``curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py``
	
	``python3.8 get-pip.py``
	
6. **Python-dev**

	For yet another unknown reason, a fresh Ubuntu 20.04 does not include the Python Development files.
	
	``sudo apt install python3-dev``
	
	
7. **Install Exo-Striker**

	At this point, your system should be clean of all problems preventing the Exo-Striker being installed. Keep in mind, your python3.8 system is likely quite "empty". To install all the dependencies in one-go, the recommended way is:
	
	``pip3.8 install git+https://github.com/3fon3fonov/exostriker --user``
	
	/for user installation -- recommended !!!!!!/
	
	Then just run:
	
	``exostriker``
	
.. NOTE :: 
	Probably the GUI screen scaling will be 150%. Go to "Change the resolution of the display" and reduce it to 100% and the GUI window will look fine.
	
**Bonus tip**

It is generally recommend to work with git clone / git pull to always get the new version - e.g.:

	``cd ~``
	
	``git clone https://github.com/3fon3fonov/exostriker``
	
	``cd exostriker``
	
	``python3.8 exostriker_gui.py``

	The latter command will open the GUI inside the root "exostriker" directory and will be easy to find your sessions and files. One can even rename the directory:

	``mv exostriker exostriker_GL486``
	
	or

	``cp -r  exostriker exostriker_GL486``
	
	``cp -r  exostriker exostriker_GL876``
	
	``cp -r  exostriker exostriker_GL1148``

	etc.,

	Your analysis of GL486 will be stored in ~/exostriker_GL486. To work and/or update the repository:

	``cd exostriker_GL486``
	
	``git pull``
	
	``python3.8 exostriker_gui.py``

	If problems occur:

	``python3.8 exostriker_gui.py -debug``

	and open an issue on the `GitHub repository`_.
	

 
------------------------------------------------------------------------------------------------------------

Common issues and solutions
....................................

If the GUI does not start after a successful installation, please try:

``python3 exostriker_gui.py -debug``

This command starts the GUI and at the same time outputs an error message with few guidelines, which are otherwise displayed in the 'stdout/stderr' tab of the GUI.

1. Broken appearance of GUI under Windows 

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


