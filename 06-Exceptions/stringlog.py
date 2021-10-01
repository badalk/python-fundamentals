# Exceptions cannot be ignored, But error codes can be
from math import log
from exceptional import convert

def string_log(s):
    # Below function returns an error code (-1) and any program that is using this function has to check for the valid error code before using the return value as expected
    # if you dont check for error codes properly, the log function throws an exception and hence error codes are unpythonic
    v = convert(s) 
    return log(v)

