############################################################
# IGNORE this section                                      #
############################################################
# not related to core part, can be safely ignored
from preface import *
text = visual.TextStim(win=win)

from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib

joystick = type('', (), {})() # Create an object to use as a name space
joystick.device = None
joystick.device_number = 0
joystick.joystickClock = core.Clock()
joystick.xFactor = 1
joystick.yFactor = 1
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
# for all keys:
text.setText((joystick.getX(), joystick.getY()))

# for some reason, all the buttons and sticks are not working for this class.

############################################################
# End routine                                              #
############################################################

############################################################
# End experiment                                           #
############################################################