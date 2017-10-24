# Hybrid-Test-Stand-Control 
Raspberry Pi based system for valve actuation and ignition. Used in UVic Rocketry's hybrid engine test stand. Fail-safe on loss of communication or power. :rocket:
## Requirements
The test stand controllers run off a server-client mode of operation, with the PC being a client and the Pi being the host. This allows control from a distance. The code for each can be found in their respective folders.

### Hardware
* Raspberry Pi (Tested on B V1.1)
* Phidgets Stepper motor controller
* Phidgets Stepper motor
* 2x Limit Switches (Pull up resistors recommended, but not required)
* Ethernet connection between client PC and Pi

### Libraries
* The test stand runs using the Phidgets API, which is included in the repo, it can be downloaded seperately [Here](https://www.phidgets.com/docs/Language_-_Python#Libraries "Phidgets Python How-To") as well. 

## Usage
**It is highly recommended you test the software on both ends before launch to ensure correct operation**\
This program was writen for the [PhidgetStepper Bipolar HC](https://www.phidgets.com/?tier=3&catid=23&pcid=20&prodid=66) and [86STH156 NEMA-34 Bipolar Gearless Stepper](https://www.phidgets.com/?tier=3&catid=24&pcid=21&prodid=355). While it should work for other steppers, its compatability with other controlers cannot be guaranteed.\ 
There are a few items of prep to do before usage:
* Firstly, calculating the rescale factor.\
  This can be calculated by `(degrees per step)*step resolution = rescalefactor`.\
  For our stepper motor, this is `1.8 degrees per step * 1/16 step resolution = 0.1125 rescale factor`.\
* Secondly ensuring you have the GIPO pins correctly set up and connected using step-up resistors on the correct pins.
* Finally, ensuring you have PuTTY on your laptop-side for backup communication.

### Testing 
A number of testing programs are provided with this softwear, for testing the software on each end of the system.
* For the stepper motor, there is [ServerSideTest](Hybrid-Test-Stand-Control/server/Lib/ServerSideTest.py) which will allow direct control and testing of the stepper motor through the Pi
* Communication between the Pi and your control laptop can be tested via [Test](Hybrid-Test-Stand-Control/server/test.py).

### Licence 
This repo is distributed under the GNU General Public License v3.0, while the Phidgets22 API is licenced under the GNU Lesser General Public License v3.0.
