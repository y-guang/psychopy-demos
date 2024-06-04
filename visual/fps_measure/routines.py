##############################
# IGNORE this section        #
##############################
# not related to core part, can be safely ignored
from preface import *
text = visual.TextStim(win=win)

##############################
# copy below                 #
##############################

##############################
# before routine             #
##############################
fps = win.getActualFrameRate()

##############################
# each frame                 #
##############################
text.setText(fps)