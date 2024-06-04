##############################
# IGNORE this section        #
##############################
# not related to core part, can be safely ignored
from preface import *
text = visual.TextStim(win=win)
trials = data.TrialHandler([], nReps=99)
##############################
# copy below                 #
##############################

##############################
# before Experiment          #
##############################
current_index = 0

##############################
# before routine             #
##############################
global current_index
text.setText(current_index)
if current_index > 3:
    trials.finished = True
current_index += 1