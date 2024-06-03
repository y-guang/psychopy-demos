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
current_time = kb.clock.getTime()
pressed = kb.getKeys(['f', 'j'], waitRelease=False, clear=False)
released = kb.getKeys(['f', 'j'], waitRelease=True, clear=True)
key_names = [p.name for p in pressed]
key_times = [p.tDown - current_time for p in pressed]

# build the str
text_contents = []
for p in pressed:
    text_contents.append(f'{p.name}: {current_time - p.tDown:.3f}')

pressed_key_text.setText('\n'.join(text_contents))