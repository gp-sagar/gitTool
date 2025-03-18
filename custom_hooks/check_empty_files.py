#!/usr/bin/env python3
import sys
import os


def check_empty(filename):
    if os.stat(filename).st_size == 0:
        print(f"{filename}: This file is empty!")
        return 1
    return 0


def main():
    return_code = 0
    for filename in sys.argv[1:]:
        return_code |= check_empty(filename)
    sys.exit(return_code)


if __name__ == "__main__":
    main()
