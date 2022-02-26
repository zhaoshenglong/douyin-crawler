import os
import logging


def check_file_exists(filename):
    return os.path.exists(filename)


def check_true(cond):
    return bool(cond)
