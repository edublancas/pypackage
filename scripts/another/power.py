"""
This script does something
"""
import argparse
from lib import math


def main(x, y):
    answer = math.power(x, y)
    print('{} ^ {} = {}'.format(x, y, answer))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate X to the power"
                                     "  of Y")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()

    main(args.x, args.y)
