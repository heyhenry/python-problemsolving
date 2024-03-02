"""
A quick program to find out the leetcodes in January's directory that hasn't been completed yet in February's leetcode directory.
"""

import os

comparison_file = os.listdir(r"E:\PYTHON\python-problemsolving\2024\January\leetcode")
new_file = os.listdir(r"E:\PYTHON\python-problemsolving\2024\February\Leetcode")

with open("todo_leetcodes.results", 'w') as nfile:

    nfile.write("Leetcodes Left from February/Leetcode: \n")

    for i in range(len(comparison_file)):
        if i != len(comparison_file) - 1 and comparison_file[i] not in new_file:
            nfile.write(comparison_file[i] + '\n')
        elif i == len(comparison_file) - 1 and comparison_file[i] not in new_file:
            nfile.write(comparison_file[i])
