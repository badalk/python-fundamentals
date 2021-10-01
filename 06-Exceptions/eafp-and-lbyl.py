# Two philosphies to handle operation failures

# EAFP - Easier to ask for forgiveness than Permissions
#   Blindly hope for the best but prepare to deal with the consequences if it does not work out
# LBYL - Look before you leap
#   Check all the preconditions of failure prone operations are met in advance of attempting the operation

# ###1- LBYL version
import os
p = '/path/to/datafile.dat'

# In below case, we are checking file exists and only then proceed with processing it
# there are few problems with this approach
#   Obvious => We only perform the existance check, what if the file contains garbage, what if the path refers to a directory instead of a file
#           According to LBYL we should add pre-emptive tests for these too
#   Subtle => It is possible that the file is deleted by another process between the check and the actual processing (Race condition)
#           There is no good way to deal with this, handling of errors from process_file would be needed in any case.
if os.path.exists(p):
    print("Processing file..")
    # process_file(p)
else:
    print('No such file as {}'.format(p))

# ###3 - More pythonic EAFP approach
import os
p = '/path/to/datafile.dat'

try:
    print("Processing file ...")
    # process_file()
except OSError as e:
    print("Could not process file because {}".format(str(e)))
