"""
A quick program to find out the leetcodes in January's directory that hasn't been completed yet in February's leetcode directory.
"""

import os

jan_leetcodes = os.listdir(r"E:\PYTHON\python-problemsolving\2024\January\leetcode")
feb_leetcodes = os.listdir(r"E:\PYTHON\python-problemsolving\2024\February\Leetcode")

with open("todo_leetcodes.results", 'w') as nfile:

    nfile.write("Leetcodes Left from January: \n")

    for i in range(len(jan_leetcodes)):
        if i != len(jan_leetcodes) - 1 and jan_leetcodes[i] not in feb_leetcodes:
            nfile.write(jan_leetcodes[i] + '\n')
        elif i == len(jan_leetcodes) - 1 and jan_leetcodes[i] not in feb_leetcodes:
            nfile.write(jan_leetcodes[i])
