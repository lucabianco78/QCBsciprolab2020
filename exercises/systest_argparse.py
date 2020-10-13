import argparse
"""Maths example with input from command line"""
parser = argparse.ArgumentParser(description="""This script gets two integers  in input 
and performs some operations on them""")
parser.add_argument("i1", type=int,
                    help="The first integer")
parser.add_argument("i2", type=int,
                    help="The second integer")


args = parser.parse_args()

i1 = args.i1
i2 = args.i2
print("{} + {} = {}".format(i1,i2, i1 + i2))
print("{} - {} = {}".format(i1,i2, i1 - i2))
print("{} * {} = {}".format(i1,i2, i1 * i2))
if i2 != 0:
    print("{} / {} = {}".format(i1,i2, i1 / i2))
else:
    print("{} / {} = Infinite".format(i1,i2))
