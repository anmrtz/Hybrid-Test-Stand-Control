# Hybrid-Test-Stand-Control
Raspberry Pi based system for valve actuation and ignition. Used in UVic Rocketry's hybrid engine test stand.
## Requirements
The test stand controllers run off a server-client mode of operation, with the PC being a client and the Pi being the host. This allows control from a distance. The code for each can be found in their respective folders.

### Hardware
* Raspberry Pi (Tested on B V1.1)
* Phidgets Stepper motor controller
* Phidgets Stepper motor
* 2x Limit Switches (Pull up resistors recommended, but not required)
* Ethernet connection between client PC and Pi

### Libraries
* The test stand runs using the Phidgets API which can be downloaded [Here](https://www.phidgets.com/docs/Language_-_Python#Libraries "Phidgets Python How-To")
