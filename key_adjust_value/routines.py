##############################
# IGNORE this section        #
##############################
# not related to core part, can be safely ignored
from preface import *
text = visual.TextStim(win=win)
polygon = visual.Line(win=win)
win.frameIntervals

##############################
# copy below                 #
##############################

##############################
# before experiment          #
##############################

##############################
# before routine             #
##############################
kb = keyboard.Keyboard()
value_to_adjust = 1.0
step = 0.01
keys_increase = ['f']
keys_decrease = ['j']
keys_watched = keys_increase + keys_decrease

##############################
# each frame                 #
##############################
pressed = kb.getKeys(keys_watched, waitRelease=False, clear=False)
released = kb.getKeys(keys_watched, waitRelease=True, clear=True)

# only one key can be pressed at a time
if len(pressed) != 1:
    kb.clearEvents()
else:
    current_time = kb.clock.getTime()
    key = pressed[0]
    if key.name in keys_increase:
        value_to_adjust += step
    else:
        value_to_adjust -= step
    polygon.setSize((value_to_adjust, value_to_adjust))
