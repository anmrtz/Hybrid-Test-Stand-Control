# Hybrid-Test-Stand-Control 
Raspberry Pi based system for valve actuation and ignition. Used in UVic Rocketry's hybrid engine test stand. Fail-safe on loss of communication or power. :rocket:

## Requirements
The test stand controllers run off a server-client mode of operation, with the PC GUI interface acting as client and the Pi server program controlling the hardware over the GPIO pins and USB. The code for each can be found in their respective folders.

### Hardware
* Raspberry Pi (Tested on B V1.1)
* 2x Phidgets Stepper motor controllers
* 2x Phidgets Stepper motors (To actuate main engine valve and vent valve)
* 4x Limit Switches (Pull up resistors recommended, but not required)
* Phidgets shaft encoder for main engine valve motor
* 2x 5V-actuated relays (To control safety valve and ignitor)
* Relay-actuated safety valve
* Ethernet connection between client PC and Pi

### Libraries
* The test stand runs using the Phidgets API, which is included in the repo, it can be downloaded seperately [Here](https://www.phidgets.com/docs/Language_-_Python#Libraries "Phidgets Python How-To") as well.
* The GUI runs on the PYQT framework. [Available here](https://www.riverbankcomputing.com/software/pyqt/download5) 
* We also use libraries that come with the standard Pi OS, inluding PI.GPIO. If you wish to emulate the pi, you must find ways to also emulate these libraries.

## Usage
**It is highly recommended you test the software on both ends before launch to ensure correct operation**
This control software was writen for stepper motors controller by the [PhidgetStepper Bipolar HC](https://www.phidgets.com/?tier=3&catid=23&pcid=20&prodid=66). 
There are a few items of prep to do before usage:
* Firstly, calculating the rescale factor.\
  This can be calculated by `(degrees per step)*step resolution = rescalefactor`.
  For our stepper motor, this is `1.8 degrees per step * 1/16 step resolution = 0.1125 rescale factor`.
* Secondly ensuring you have the GIPO pins correctly set up and connected using step-up resistors on the correct pins.
* Finally, ensuring you have PuTTY on your laptop-side for backup communication.

### Licence 
This repo is distributed under the GNU General Public License v3.0, while the Phidgets22 API is licenced under the GNU Lesser General Public License v3.0.
