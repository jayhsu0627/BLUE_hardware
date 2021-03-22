# For OS functions
import time
import spidev
from evdev import InputDevice, categorize, ecodes
import numpy as np



# Convert all numpy array into hex
np.set_printoptions(formatter={'int':hex})

# Subfunction - Log file
# @brief Logs message to log file
# also handles checks for the shutdown command
def spiSend_G29_Command(info,msgSize):
    return

# INIT and CONFIGURE SPI
spi = spidev.SpiDev()
spi.open(2,0)
spi.max_speed_hz = 3000000
spi.mode = 2

# creates object gamepad
gamepad = InputDevice('/dev/input/event0')

# prints out device info at start
# print(gamepad)


# MAIN LOOP
if gamepad:
    # Clear display

    for event in gamepad.read_loop():
        if event.type == ecodes.EV_ABS:
        # absevent = categorize(event)
            # print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
#            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
#		msg = np.array([event.value]).tobytes()
		msg = [int(event.value)]
#		print(event,"value:",msg)
#		print("msg,",msg)
                spi.xfer2(msg)
else:
    print("Gamepad is missing, please check your joystick connection.")
