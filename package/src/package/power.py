"""
This script does something
"""
import argparse
from package import math


def print_power(x, y):
    answer = math.power(x, y)
    print('{} ^ {} = {}'.format(x, y, answer))


def main():
    parser = argparse.ArgumentParser(description="calculate X to the power"
                                     "  of Y")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()

    print_power(args.x, args.y)


if __name__ == '__main__':
    main()
