############################################################
# IGNORE this section                                      #
############################################################
# not related to core part, can be safely ignored
from preface import *
text = visual.TextStim(win=win)

from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
numJoysticks = joysticklib.getNumJoysticks()
button_resp = type('', (), {})() # Create an object to use as a name space
button_resp.device = None
button_resp.device_number = 0
button_resp.device = joysticklib.Joystick(0)
button_resp.keys:list = []
############################################################
# NOTE: COPY AFTER THIS LINE ONLY                          #
############################################################

############################################################
# Before experiment                                        #
############################################################


############################################################
# Begin experiment                                         #
############################################################

############################################################
# Begin routine                                            #
############################################################

############################################################
# Each frame                                               #
############################################################
# NOTE: try very careful about this.
# if set store all key the button_resp.keys is **array**
# if set store last key the button_resp.keys is **int**
# I tend to believe it is an bug in the psychopy library.

# for all keys:
if button_resp.keys != None and len(button_resp.keys) > 0:
    text.setText(button_resp.keys)

# for last key:
if button_resp.keys != None:
    text.setText(button_resp.keys)

# the result
key_map: dict = {
    0: 'A',
    1: 'B',
    2: 'X',
    3: 'Y',
    4: 'LB',
    5: 'RB',
    6: 'View',
    7: 'Menu',
    8: 'LStick',
    9: 'RStick',
}

############################################################
# End routine                                              #
############################################################

############################################################
# End experiment                                           #
############################################################