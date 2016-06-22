"""
Module contaning class which map stdin and/or
stdio and/or stderr to file, file names are optional

-----usage------
remember to assign constructor to a variable with a
valid scope, For ex
import [package.]nonstd
var_name = nonstd.IO(), calling just nonstd.IO() will force the
destructor to be executed.

This doesn't work / is not as usable,
file gets closed in next line
with open("input.txt","r") as file:
    sys.stdin = file
print(input())
"""

import sys

class IO:
    """maps std in, out and err to files

    default filnames :
    stdin = input.txt
    stdout = tc_output.txt
    stderr = error.txt
    """

    def __init__(self, in_file="input.txt", out_file="output.txt", err_file=None):
        try:
            sys.stdin = self.in_file = open(in_file, "r")
            sys.stdout = self.out_file = open(out_file, "w")
            if err_file is not None:
                sys.stderr = self.err_file = open(err_file, "w")
                self.err_file = err_file
            else:
                self.err_file = None
            self.initialized = True
        except Exception:
            print("could not read or create a file. \nFile paths", "\n", in_file, "\n", out_file, "\n")
            self.initialized = False
            self.cleanup()

    def __del__(self):
        if not self.initialized:
            return
        sys.stdin = sys.__stdin__
        self.in_file.close()
        sys.stdout = sys.__stdout__
        self.out_file.close()
        if self.err_file is not None:
            sys.stderr = sys.__stderr__
            self.err_file.close()

    def cleanup(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        if self.err_file is not None:
            sys.stderr = sys.__stderr__


class In:
    """maps std in to file

    default filname :
    stdin = input.txt
    """
    def __init__(self, in_file="input.txt"):
        try:
            sys.stdin = self.in_file = open(in_file, "r")
            self.initialized = True
        except FileNotFoundError:
            print("file not found or unreadable", in_file)
            sys.stdin = sys.__stdin__
            self.initialized = False

    def __del__(self):
        if not self.initialized:
            return
        sys.stdin = sys.__stdin__
        self.in_file.close()



class Out:
    """maps std out to files

    default filname :
    stdout = tc_output.txt
    """

    def __init__(self, out_file="output.txt"):
        try:
            sys.stdout = self.out_file = open(out_file, "w")
            self.initialized = True
        except Exception:
            print("could not create or write to file", out_file)
            sys.stdout = sys.__stdout__
            self.initialized = False

    def __del__(self):
        if not self.initialized:
            return
        sys.stdout = sys.__stdout__
        self.out_file.close()


class Err:
    """maps std err to files

    default filname :
    stderr = error.txt
    """

    err_file = None

    def __init__(self, err_file="error.txt"):
        try:
            sys.stderr = self.err_file = open(err_file, "w")
            self.initialized = True
        except Exception:
            print("could not create or write to error file in", err_file)
            self.initialized = False
            sys.stderr = sys.__stderr__

    def __del__(self):
        if not self.initialized:
            return
        sys.stderr = sys.__stderr__
        self.err_file.close()
