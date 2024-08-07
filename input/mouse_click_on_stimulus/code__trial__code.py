########################################################################################################################
# Prologue
# It is auto generated. DO NOT MODIFY THE COMMENT.
# This part will NOT be synced and executed. Add what you want to make the language server happy.
########################################################################################################################
from code__preface import *
mouse = event.Mouse()
from psychopy.visual.polygon import Polygon
polygon = Polygon(win=win)
polygon_2 = Polygon(win=win)
text = visual.TextStim(win=win)
########################################################################################################################
# Before Experiment
# It is auto generated. DO NOT MODIFY THE COMMENT
########################################################################################################################

########################################################################################################################
# Begin Experiment
# It is auto generated. DO NOT MODIFY THE COMMENT
########################################################################################################################

########################################################################################################################
# Begin Routine
# It is auto generated. DO NOT MODIFY THE COMMENT
########################################################################################################################

########################################################################################################################
# Each Frame
# It is auto generated. DO NOT MODIFY THE COMMENT
########################################################################################################################
mouse_pos = mouse.getPos()

# NOTE: following tow does not works properly as the unit is not the same!
# context = f"Pos {mouse_pos}\n \
#     In left: {polygon.contains(x = mouse_pos[0], y = mouse_pos[1])}\n \
#     In right: {polygon_2.contains(x = mouse_pos[0], y = mouse_pos[1])}"
# context = f"Pos {mouse_pos}\n \
#     In left: {polygon.contains(x = mouse_pos)}\n \
#     In right: {polygon_2.contains(x = mouse_pos)}"

# Recommended way
context = f"Pos {mouse_pos}\n \
    In left: {polygon.contains(mouse)}\n \
    In right: {polygon_2.contains(mouse)}"
text.setText(context)

########################################################################################################################
# End Routine
# It is auto generated. DO NOT MODIFY THE COMMENT
########################################################################################################################

########################################################################################################################
# End Experiment
# It is auto generated. DO NOT MODIFY THE COMMENT
########################################################################################################################

