import serial
import sys
import time

assert sys.version_info > (2,7)
assert sys.version_info < (2,8)

class RobotVacuumCleaner:
   def __init__(self):
      self.ser = serial.Serial(port='/dev/serial0', baudrate=115200)

   def writeSerialString(self, writeData):
      self.ser.write(writeData)

   def readSerialString(self, size):
      return self.ser.read(size)

   # Returns an integer in the range [0,255]
   def readU8(self):
      return ord(self.ser.read(1))

   # Returns an integer in the range [-128,127]
   def readI8(self):
      unsignedByte = self.readU8()
      if unsignedByte > 127:
         return unsignedByte - 256
      else:
         return unsignedByte

   # Returns an integer in the range [0,65535]
   # Assumes high byte is sent first
   def readU16(self):
      highByte = self.readU8()
      lowByte = self.readU8()
      return (highByte << 8) | lowByte

   # Returns an integer in the range [-32768,32767]
   def readI16(self):
      unsignedWord = self.readU16()
      if unsignedWord > 32767:
         return unsignedWord - 65536
      else:
         return unsignedWord

   def reset(self):
      self.writeSerialString(chr(7))
      self.ser.timeout = 10 # wait no more than 10 seconds
      while True:
         line = self.ser.readline()
         if len(line) == 0:
            break
         print line
      self.ser.timeout = None

   def start(self):
      self.writeSerialString(chr(128))

   def stop(self):
      self.writeSerialString(chr(173))

   def safe(self):
      self.writeSerialString(chr(131))

   # sensorsList must be a set, list, tuple, etc. of integers
   def querySensors(self, sensorsList):
      serialString = chr(149) # Opcode
      serialString += chr(len(sensorsList))
      for sensor in sensorsList:
         serialString += chr(sensor)
      self.writeSerialString(serialString)

   def moveForward(self, velocity, duration):
      lowerByte = velocity & 255
      upperByte = (velocity >> 8) & 255
      self.writeSerialString(chr(132))
      self.writeSerialString(chr(137) + chr(upperByte) + chr(lowerByte) + chr(0) + chr(0))
      time.sleep(duration)
      self.writeSerialString(chr(137) + chr(0) + chr(0) + chr(0) + chr(0))

   def controlWheels(self, leftPwm, rightPwm, duration):
      rightLowerByte = rightPwm & 255
      rightUpperByte = (rightPwm >> 8) & 255
      leftLowerByte = leftPwm & 255
      leftUpperByte = (leftPwm >> 8) & 255
      self.writeSerialString(chr(146) + chr(rightUpperByte) + chr(rightLowerByte) + chr(leftUpperByte) + chr(leftLowerByte))
      time.sleep(duration)
      self.writeSerialString(chr(146) + chr(0) + chr(0) + chr(0) + chr(0))
 
   def turnRight(self, velocity, duration):
      velocityLowerByte = velocity & 255
      velocityUpperByte = (velocity >> 8) & 255
      self.writeSerialString(chr(137) + chr(velocityUpperByte) + chr(velocityLowerByte) + chr(255) + chr(255))
      time.sleep(duration)
      self.writeSerialString(chr(137) + chr(0) + chr(0) + chr(0) + chr(0))

   def controlMotors(self, enableSideBrush, enableVacuum, enableMainBrush):
      motors = 0
      motors = (motors | 1) if enableSideBrush else motors
      motors = (motors | 2) if enableVacuum else motors
      motors = (motors | 4) if enableMainBrush else motors
      print motors
      self.writeSerialString(chr(138) + chr(motors))

   def readEncoderValues(self):
      self.querySensors((43, 44))
      return (self.readU16(), self.readU16())

   def readAngleSensor(self):
      self.querySensors((20,))
      return self.readI16()

