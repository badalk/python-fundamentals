# ###1 Basic exception handling

from exceptional import convert # Throws indentation error when any block of code is empty
convert("33") # works
convert("hedgehog") # throws ValueError

# ###2 Feeding object of another type into the module function
convert([33,44,55]) # throws TypeError and our code did not handle the exceptions

# ###3 Imprudent Error Codes
from stringlog import string_log
string_log("ouch")