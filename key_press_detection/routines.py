##############################
# IGNORE this section        #
##############################
# not related to core part, can be safely ignored
from preface import *
pressed_key_text = visual.TextStim(win=win)

##############################
# copy below                 #
##############################

##############################
# before routine             #
##############################

kb = keyboard.Keyboard()

##############################
# each frame                 #
##############################

pressed = kb.getKeys(['f', 'j'], waitRelease=False, clear=False)
released = kb.getKeys(['f', 'j'], waitRelease=True, clear=True)
key_names = [p.name for p in pressed]
pressed_key_text.setText(','.join(key_names))