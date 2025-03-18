#!/usr/bin/env python3
import sys


def check_todo_comments(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    for line_number, line in enumerate(lines, 1):
        if "TODO" in line:
            print(f"{filename}:{line_number}: Found TODO comment")
            return 1
    return 0


def main():
    return_code = 0
    for filename in sys.argv[1:]:
        return_code |= check_todo_comments(filename)
    sys.exit(return_code)


if __name__ == "__main__":
    main()
