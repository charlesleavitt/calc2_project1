# File Project1.py
# authors: Charles Leavitt, Simon Buchheit, Emily Wu, Stephanie Huang
# dependencies: Requires python3, python3-tk, pip,and matplotlib.
#   to install:     sudo apt install python3
#                   sudo apt install python3-tk
#                   sudo apt install python3-pip
#                   sudo pip3 install matplotlib
#
# Usage: python3 project1.py

import matplotlib.pyplot as plt


def do_the_maths(n,k,p0):
    """
    Purpose: this function computes a sequence of the form: P(n+1) = (k)(Pn)(1-Pn)
    Input:  n - the number of values to compute
            k - the constant value
            p0 - the value of the sequence at P at n = 0
    Returns: the sequence Pn
    """
    Pn = [p0]  # initialize an array to represent a sequence starting with p0
    for i in range(0,n):                        # loop for n times
        Pn_plus_1 = (k) * Pn[i] * (1 - Pn[i])   # computes Pn+1 = (k)(Pn)(1-Pn)
        Pn.append(Pn_plus_1)                    # adds the Pn+1 to sequence
    return Pn                                   # returns the sequence


def clean_input(k1,p0):
    """Properly formats input if given as fraction, returns values as floats"""
    if "/" in k1 :
        nums = k1.split('/')
        k1 = (float(nums[0]) / float(nums[1]))
    else:
        k1 = float(k1)
    if "/" in p0:
        nums = p0.split('/')
        p0 = (float(nums[0]) / float(nums[1]))
    else:
        p0 = float(p0)
    return k1,p0


def main():
    """
    This is the main function that:
    1) prompts the user for values
    2) call the function to compute the sequence of the values
    3) plots the sequence
    """
    print("values can entered as: 1.5 or 3/2")
    n = int(input("enter number of terms 'n': "))   # prompt user for n value
    k = input("enter value for k: ")                # prompt user for k value
    p0 = input("enter the value of P0: ")           # prompt user for P0 value
    plt.title(str(n)+ " terms of Sequence: P(n+1) = (k)(Pn)(1-Pn)\nwith k= " + str(k) + " and P0= " + str(p0))
    k1,p0 = clean_input(k,p0)           # handles values given as fractions
    sequence = do_the_maths(n,k1,p0)    # compute the sequence
    print (sequence)                    # print number value of sequence
    plt.plot(sequence, 'ro')            # graphs the sequence
    plt.xlabel('X-axis')                # labels
    plt.ylabel('Y-axis')                # labels
    plt.show()                          # displays the sequence graph

main()  # runs the code

