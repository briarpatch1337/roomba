from RobotVacuumCleaner import *

rob = RobotVacuumCleaner()

rob.readAngleSensor()
leftStart, rightStart = rob.readEncoderValues()

rob.turnRight(200, 1.05)
leftEnd, rightEnd = rob.readEncoderValues()

print float(leftEnd - leftStart)
print float(rightStart - rightEnd)


time.sleep(1)
print rob.readAngleSensor()


