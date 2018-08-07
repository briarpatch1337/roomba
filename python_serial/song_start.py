import serial
import time

# Open a serial connection to Roomba
ser = serial.Serial(port='/dev/ttyAMA0', baudrate=115200)

# Start
# ser.write(chr(128))
# time.sleep(.1)

# Enter safe mode
ser.write(chr(131))
time.sleep(.1)

# Program a song into Roomba.
song1 = (chr(10) +
   chr(74) + chr(30) +
   chr(73) + chr(30) +
   chr(72) + chr(20) +
   chr(72) + chr(20) +
   chr(72) + chr(20) +
   chr(71) + chr(30) +
   chr(70) + chr(30) +
   chr(69) + chr(30) +
   chr(69) + chr(15) +
   chr(69) + chr(15)
)

song2 = (chr(11) +
   chr(68) + chr(30) +
   chr(67) + chr(30) +
   chr(65) + chr(10) +
   chr(67) + chr(10) +
   chr(65) + chr(10) +
   chr(64) + chr(15) +
   chr(65) + chr(15) +
   chr(67) + chr(30) +
   chr(65) + chr(30) +
   chr(64) + chr(30) +
   chr(0)  + chr(30)
)

song3 = (chr(11) +
   chr(74) + chr(30) +
   chr(73) + chr(30) +
   chr(72) + chr(20) +
   chr(72) + chr(20) +
   chr(72) + chr(20) +
   chr(71) + chr(30) +
   chr(70) + chr(30) +
   chr(69) + chr(15) +
   chr(69) + chr(15) +
   chr(0)  + chr(15) +
   chr(69) + chr(15)
)

song4 = (chr(10) +
   chr(67) + chr(30) +
   chr(65) + chr(30) +
   chr(64) + chr(10) +
   chr(65) + chr(10) +
   chr(64) + chr(10) +
   chr(62) + chr(15) +
   chr(64) + chr(15) +
   chr(65) + chr(30) +
   chr(64) + chr(30) +
   chr(62) + chr(60)
)

ser.write(chr(140) + chr(0) + song1)
ser.write(chr(140) + chr(1) + song2)
ser.write(chr(140) + chr(2) + song3)
ser.write(chr(140) + chr(3) + song4)

# Play the song we just programmed.
ser.write(chr(141) + chr(0))
ser.flush()
time.sleep(3.75) # wait for the song to complete
ser.write(chr(141) + chr(1))
ser.flush()
time.sleep(3.75) # wait for the song to complete
ser.write(chr(141) + chr(2))
ser.flush()
time.sleep(3.75) # wait for the song to complete
ser.write(chr(141) + chr(3))
ser.flush()
time.sleep(3.75) # wait for the song to complete

# Leave the Roomba in passive mode; this allows it to keep
#  running Roomba behaviors while we wait for more commands.
ser.write('\x80')

# Close the serial port; we're done for now.
ser.close()
