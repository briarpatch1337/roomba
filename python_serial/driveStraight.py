from RobotVacuumCleaner import *

rob = RobotVacuumCleaner()

leftStart, rightStart = rob.readEncoderValues()
rob.controlWheels(100, 96, 2)
leftEnd, rightEnd = rob.readEncoderValues()

rightOverdrive = (float(rightEnd - rightStart) / float(leftEnd - leftStart))
print rightOverdrive

rob.controlWheels(100, int(float(96) / rightOverdrive), 2)
print int(float(92) / rightOverdrive)

leftStart = leftEnd
rightStart = rightEnd
leftEnd, rightEnd = rob.readEncoderValues()

verifyRightOverdrive = (float(rightEnd - rightStart) / float(leftEnd - leftStart))
print verifyRightOverdrive



