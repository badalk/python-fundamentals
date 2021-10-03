# try ... finally lets you clean up whether an exception occurs or not

import os
import sys
def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    os.mkdir(dir_name) # what if there is an execption, it will not change back the current working directory to its original path, as the next statement does not execute
    os.chdir(original_path)

# ###1 Finally block usage
def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name) 
    except OSError as e: #following code in the finally block still executes even if there is an exception raised.
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)