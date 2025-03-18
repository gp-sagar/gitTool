#!/usr/bin/env python3
import sys


def check_header(filename):
    with open(filename, "r") as f:
        first_line = f.readline()
    if "Copyright" not in first_line:
        print(f"{filename}: Missing license header!")
        return 1
    return 0


def main():
    return_code = 0
    for file in sys.argv[1:]:
        return_code |= check_header(file)
    sys.exit(return_code)


if __name__ == "__main__":
    main()
