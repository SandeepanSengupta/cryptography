# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 14:33:27 2017

@author: Tamojit
"""

class Serial:

    def __intit__(self,port,baudrate):
        self.port=port
        self.baudrate = baudrate

    def begin(self,p,br,timeout=None):
        import time
        import serial
        self.baudrate =  br
        self.port = p
        self.timeout = timeout
        self.ser = serial.Serial(self.port,self.baudrate,timeout=self.timeout)
        self.ser.close()
        self.ser.open()
        time.sleep(2)

    def sprint(self, data):
        import time
        self.ser.write(str(data))
        time.sleep(0.25)

    def sprintln(self, data):
        import time
        self.ser.write(str(data)+"\n")
        time.sleep(0.25)

    def sread(self):
        self.readData = str(self.ser.read(self.ser.inWaiting()))
        return self.readData

    def closePort(self):
        self.ser.close()

    def openPort(self):
        self.ser.open()
#mySerial = Serial()
