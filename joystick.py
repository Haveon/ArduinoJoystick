import serial

class Joystick:
    def __init__(self, port='/dev/ttyACM0', baud=9600):
        self.ser = serial.Serial(port=port, baudrate=baud)
        self.state = [0,0,0]
        return

    def _updateState(self):
        self.ser.write('1') #It should only write one byte!
        line = self.ser.readline()
        self.state = map(int,line[:-2].split(','))

    def getState(self):
        self._updateState()
        return self.state

    def getCoords(self):
        self._updateState()
        x = self.state[0]
        y = self.state[1]
        return x,y

    def getButtonState(self):
        self._updateState()
        sel = self.state[2]
        return sel

if __name__ == '__main__':
    joy = Joystick('/dev/ttyACM0')
    while True:
        print joy.getState()