from RobotVacuumCleaner import *

rob = RobotVacuumCleaner()

rob.querySensors((21, 22, 23, 24, 25, 26, 35))

chargingState = rob.readU8() & 0x7
voltage = rob.readU16()
current = rob.readI16()
temperature = rob.readI8()
batteryCharge = rob.readU16()
batteryCapacity = rob.readU16()
batteryChargePercent = float(batteryCharge) / float(batteryCapacity) * 100.0
oiMode = rob.readU8() & 0x3

print "Charging state: %d" % chargingState
print "OI Mode: %d" % oiMode
print "Voltage: %f V" % (float(voltage) / 1000.0)
print "Current: %f A" % (float(current) / 1000.0)
print "Temperature: %d deg C" % temperature 
print "Battery Charge: %d mAh (%f%%)" % (batteryCharge, batteryChargePercent)
print "Battery Capacity: %d mAh" % batteryCapacity

