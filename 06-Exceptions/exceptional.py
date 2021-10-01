# Exceptions are means of control flow
# difficult to demonstrate on REPL

# '''A module for demonstrating exception'''
# def convert(s):
#     '''Convert to an integer'''
#     x = int(s)
#     return x

# def convert(s):
#     try:
#         x = int(s)
#         print("Convertion succeeded ! x= ", x)
#     except ValueError:
#         print("Convertion Failed !!!")
#         x = -1
#     except TypeError:
#         print("Convertion Failed !!!")
#         x = -1
#     return x
        
# def convert(s):
#     x = -1
#     try:
#         x = int(s)
#         print("Convertion succeeded ! x= ", x)
#     except (ValueError, TypeError):
#         print("Convertion Failed !!!")
#     return x

# ###3 Empty Indentation Error and pass statement
# BESTPRACTICE You should not normally catch IndentationError, SyntaxError or NameError
# def convert(s):
#     x = -1
#     try:
#         x = int(s)
#     except (ValueError, TypeError):
#         pass # Does nothing. Allows you to construct syntactically permissible blocks which are symantically empty
#     return x

# ###4 except object to deal with excpetions and return error code -1
# import sys

# def convert(s):
#     x = -1
#     try:
#         x = int(s)
#     except (ValueError, TypeError) as e:
#         print ("Convertion error: {}".format(str(e)), file=sys.stderr )

#     return x


# ###5 raise an exception, instead of error code
import sys

def convert(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print ("Convertion error: {}".format(str(e)), file=sys.stderr )
        raise #re-raises the exception currently being handled

