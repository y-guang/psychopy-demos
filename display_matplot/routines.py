##############################
# IGNORE this section        #
##############################
# not related to core part, can be safely ignored
from preface import *
image = visual.ImageStim(win=win)

# pseudo code
y: list = list(range(10))
x: list = list(range(10))

##############################
# copy below                 #
##############################

##############################
# before routine             #
##############################
import matplotlib.pyplot as plt

# pseudo code
y: list = list(range(10))
x: list = list(range(10))

# plot here
plt.figure()
plt.plot(x, y)
plt.savefig('./data/temp.png')
plt.close()

# display image
image.setImage('./data/temp.png')

##############################
# each frame                 #
##############################