# circuitpython-whadda-rudolph
## Required hardware
* [Whadda Rudolf XL Soldering & Programming Kit](https://whadda.com/product/rudolf-xl-soldering-programming-kit-wspxl101/)
* [Arduino Nano RP2040 Connect](https://docs.arduino.cc/hardware/nano-rp2040-connect)
* USB Power supply

## Soldering
Note that the Whadda by default uses the 5V (VUSB) pin to power the Arduino, this is not an issue on the Arduino Nano Every but on the Arduino Nano RP2040 Connect this is not working. So make sure the solder bridge on the bottom of the RP2040 Connect is not bridged and create a wire bridge between 5V(VUSB) pin and the VIN pin.
  
## Setup and configuration
*
The follwing Circuitpython libraries are required:
* neopixel
* adafruit_fancyled

## References
* https://learn.adafruit.com/fancyled-library-for-circuitpython

