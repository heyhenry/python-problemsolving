"""
A quick program to find out the leetcodes in January's directory that hasn't been completed yet in February's leetcode directory.
"""

import os

jan_leetcodes = os.listdir(r"E:\PYTHON\python-problemsolving\2024\January\leetcode")
feb_leetcodes = os.listdir(r"E:\PYTHON\python-problemsolving\2024\February\Leetcode")

to_do_leetcodes = []

for i in jan_leetcodes:
    if i not in feb_leetcodes:
        to_do_leetcodes.append(i)

print(to_do_leetcodes)