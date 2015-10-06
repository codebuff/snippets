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
    stdout = output.txt
    stderr = error.txt
    """

    in_file = None
    out_file = None
    err_file = None

    def __init__(self, in_file="input.txt", out_file="output.txt", err_file="error.txt"):
        sys.stdin = self.in_file = open(in_file, "r")
        sys.stdout = self.out_file = open(out_file, "w")
        sys.stderr = self.err_file = open(err_file, "w")

    def __del__(self):
        sys.stdin = sys.__stdin__
        self.in_file.close()
        sys.stdout = sys.__stdout__
        self.out_file.close()
        sys.stderr = sys.__stderr__
        self.err_file.close()


class In:
    """maps std in to file

    default filname :
    stdin = input.txt
    """

    in_file = None

    def __init__(self, in_file="input.txt"):
        sys.stdin = self.in_file = open(in_file, "r")

    def __del__(self):
        sys.stdin = sys.__stdin__
        self.in_file.close()


class Out:
    """maps std out to files

    default filname :
    stdout = output.txt
    """

    out_file = None

    def __init__(self, out_file="output.txt"):
        sys.stdout = self.out_file = open(out_file, "w")

    def __del__(self):
        sys.stdout = sys.__stdout__
        self.out_file.close()


class Err:
    """maps std err to files

    default filname :
    stderr = error.txt
    """

    err_file = None

    def __init__(self, err_file="error.txt"):
        sys.stderr = self.err_file = open(err_file, "w")

    def __del__(self):
        sys.stderr = sys.__stderr__
        self.err_file.close()
