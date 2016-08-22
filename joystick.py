import serial
from multiprocessing import Process, Array

class Joystick:
    def __init__(self, port='/dev/ttyACM0', baud=9600):
        ser = serial.Serial(port=port, baudrate=baud)
        self.state = Array('i', [0,0,0])
        p = Process(target=self._busyLoop, args=(ser, self.state))
        p.start()
        return

    def _busyLoop(self, ser, data):
        while True:
            line = ser.readline()
            tmp = line[:-2].split(',')
            print tmp
            data[0] = int(tmp[0])
            data[1] = int(tmp[1])
            data[2] = int(tmp[2])
        return

    def getCoords(self):
        x = self.state[0]
        y = self.state[1]
        return x,y

    def getButtonState(self):
        sel = self.state[2]
        return sel

if __name__ == '__main__':
    joy = Joystick()
    #print joy.getCoords()