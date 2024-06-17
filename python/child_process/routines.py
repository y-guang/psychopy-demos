############################################################
# IGNORE this section                                      #
############################################################
# not related to core part, can be safely ignored
from preface import *
text = visual.TextStim(win=win)

############################################################
# NOTE: COPY AFTER THIS LINE ONLY                          #
############################################################

############################################################
# Before experiment                                        #
############################################################

import subprocess
import time
import os

# for testing purpose, it is safe to ignore this
from script import get_shared_memory, read_shared_memory, close_shared_memory

# create a child process
current_script_directory = os.path.dirname(os.path.abspath(__file__))

child = subprocess.Popen(['python', 'script.py'], cwd=current_script_directory, text=True)

# wait for the child process to start
time.sleep(1)

# get the shared memory
shared_memory = get_shared_memory()



############################################################
# Begin experiment                                         #
############################################################

############################################################
# Begin routine                                            #
############################################################
# read the shared memory
text.setText(read_shared_memory(shared_memory))

# following part can be use when no PsychoPy is involved
# for _ in range(10):
#     print(read_shared_memory(shared_memory))
#     time.sleep(1)
############################################################
# Each frame                                               #
############################################################

############################################################
# End routine                                              #
############################################################

############################################################
# End experiment                                           #
############################################################

# close the shared memory
close_shared_memory(shared_memory)
# kill the child process
child.terminate()
# wait for the child process to exit
child.wait()