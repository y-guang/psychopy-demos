"""
Create an named shared memory with windows api. You can just treat it as do some random stuff allow us to test creating child process in python.
"""
import mmap
import time
import struct

SIZE = 1024
NAME = "Local\\PsychoPyShared"

# open the shared memory
if __name__ == "__main__":
    shared_memory = mmap.mmap(fileno=-1,
                              length=SIZE,
                              tagname=NAME,
                              access=mmap.ACCESS_WRITE,)

    # inf loop write to the shared memory
    cnt = 0
    try:
        while True:
            shared_memory.seek(0)
            shared_memory.write(struct.pack('i', cnt))
            time.sleep(1)
            cnt += 1
    finally:
        shared_memory.close()

def get_shared_memory():
    return mmap.mmap(fileno=-1,
                     length=SIZE,
                     tagname=NAME,
                     access=mmap.ACCESS_READ,)

def read_shared_memory(shared_memory):
    shared_memory.seek(0)
    return struct.unpack('i', shared_memory.read(4))[0]

def close_shared_memory(shared_memory):
    shared_memory.close()
