"""
A quick program to find out the leetcodes in January's directory that hasn't been completed yet in February's leetcode directory.
"""

import os

jan_leetcodes = os.listdir(r"E:\PYTHON\python-problemsolving\2024\January\leetcode")
feb_leetcodes = os.listdir(r"E:\PYTHON\python-problemsolving\2024\February\Leetcode")
feb_r02_leetcodes = os.listdir(r"E:\PYTHON\python-problemsolving\2024\February\Leetcode_round_two")

with open("todo_leetcodes.results", 'w') as nfile:

    nfile.write("Leetcodes Left from February/Leetcode: \n")

    for i in range(len(feb_leetcodes)):
        if i != len(feb_leetcodes) - 1 and feb_leetcodes[i] not in feb_r02_leetcodes:
            nfile.write(feb_leetcodes[i] + '\n')
        elif i == len(feb_leetcodes) - 1 and feb_leetcodes[i] not in feb_r02_leetcodes:
            nfile.write(feb_leetcodes[i])
