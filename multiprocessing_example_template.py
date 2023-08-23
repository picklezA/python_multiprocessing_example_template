# this program is for testing and demonstration

# multiprocessing should be auto included in 
from multiprocessing import Process
import os
import time

# this will be the target function that you want the process to do,
# you can provide multiple arguments to a given function
def my_function(name):
    
    # this is for demonstration purposes
    if name == "john":
        time.sleep(3)
    # notice that individual processes when declared have unique windows/linux process IDs
    print("hello " + name + "!  [ProcessID:" + str(os.getpid()) + "]")
    
# alternatively, you can initialize multiple processes in a callable function
def other_way_to_start_processes(name1, name2):
    # declare processes as objects in memory
    proc2 = Process(target=my_function, args=(name1,))
    proc3 = Process(target=my_function, args=(name2,))
    # this will start each individual process
    proc2.start()
    proc3.start()
    # this will wait for initialized processes to rejoin the main process
    proc2.join()
    proc3.join()
    # note: in python, if you want to declare processes and threads you need to
    # declare processes first then you can deploy threads in a separate function
    
# process initialization needs to happen within here, it won't work in python otherwise
# __main__ is the default ID/function name for a python script
if __name__ == "__main__":
    
    # you will need to initialize it as an object with passed arguments
    proc1 = Process(target=my_function, args=("bob",))
    
    # in order to initialize the process, you need to use .start()
    proc1.start()
    
    # when a process is done running, we need this process to rejoin
    # the main process. to do so, use .join()
    proc1.join()
    # code found after this will not run until the process rejoins the main process
    
    print("Process 1 is done!")
    
    # we can also initialize processes inside a function!
    other_way_to_start_processes("linda", "john")
    
    print("Process 2 & 3 are done!")
    
# the global interpreter lock will prevent processes from sharing memory space
# and variable contents between themselves