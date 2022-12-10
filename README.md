# circuitpython-whadda-rudolph
## Required hardware
* [Arduino Nano RP2040 Connect](https://docs.arduino.cc/hardware/nano-rp2040-connect)
* [Whadda Rudolf XL Soldering & Programming Kit](https://whadda.com/product/rudolf-xl-soldering-programming-kit-wspxl101/)
* USB Power supply

## Setup and configuration



## Customization


### Delay
You can change the delay between updates of led's with the `DELAY` variable (seconds); set it anywhere from `0` to `~`, the default is 0.5 seconds.

### Brightness
You can change the brightness of the led's with the `BRIGHTNESS` variable; set it anywhere from `1` to `100`, the default is 8.
You'll find that 100 is _extremely bright_ and even 8 (default) is bright enough if the tree is on your desk :)

### Start time and stop time
If you want the Xmas Tree only to blink during the day (or other time range) you can configure at what time it starts and stops blinking with the
`STARTTIME` and `STOPTIME` variable; set these variables anywhere from `0000` to `2359`. The default are 0000 and 2359

