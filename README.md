# ArduinoJoystick

This project has three parts working together: hardware, stick.ino and joystick.py

### Dependencies
It has been tested and working under Python 2.7.6.

It requires PySerial

### Hardware:
We're using an arduino micro and adafruit's 2-axis joystick (https://www.adafruit.com/products/512)

The arduino is powered by the computer through the usb connection. The x-axis potentiometer is wired to pin A0, while the y-axis wired to pin A1. The push button is wired to pin 7. We use the ground and 5V pins from the arduino to power the joystick.

### Software

#### stick.ino

The script is fairly straightforward. 

The setup function just opens up a serial connection at 9600 baud. 

The loop function checks this connection for any bytes to process. If there is at least one byte, it will proceed through the rest of the function. One byte is removed from the buffer and then the various values are read from the joystick. X and Y are ints between 0 and 1023. When the stick is idle, x and y normally read 515 and 501 respectively. These values are subtracted from the read x,y coords such that 0,0 becomes the new default. The push button returns 0 when being pressed and 1 otherwise. This is reversed before sending the data through the serial connection such that if the button is being pushed it will report 1.

TODO: If more than one byte is in the buffer waiting to be read, then the arduino will send multiple lines of data, one for each byte. This happens because we aren't emptying the buffer inside the if statement, just removing one byte. This should be fixed at some point.


#### joystick.py

This file contains a Joystick class.

It is initialized with the port the arduino is connected to and baud rate. It will then establish a serial connection to the arduino. The state of the joystick is kept in a list, the first and second positions are ints recording the x and y position, while the third is an int recording the state of the button. There are three different public methods:

* getState: [no arguments] Returns a list with the state of the joystick
* getCoords: [no arguments] Returns a tuple with the x and y coordinates
* getButtonState: [no arguments] Returns an int with the state of the button, 1 if pressed 0 otherwise.

There is one private method: updateState. This method is called internally whenever any of the other methods are called. It will write one byte to the arduino and then listen for the response containing the state of the joystick. It will process the string and update the state attribute.
