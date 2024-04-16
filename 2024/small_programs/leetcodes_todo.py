"""
A quick program to find out the leetcodes in January's directory that hasn't been completed yet in February's leetcode directory.
"""

import os

comparison_file = os.listdir(r"E:\PYTHON\python-problemsolving\2024\March\Leetcode")
new_file = os.listdir(r"E:\PYTHON\python-problemsolving\2024\April\Leetcode")
leetcodes_file = r"E:\PYTHON\python-problemsolving\2024\small_programs\todo_leetcodes.results"

count = 0

with open(leetcodes_file, 'r') as file:
    read_content = file.read()
    if read_content:
        splitlines = read_content.splitlines()
        
        for row in splitlines:
            if row[0].isnumeric():
                count += 1

with open(leetcodes_file, 'w') as nfile:

    nfile.write("Leetcodes Questions To Do: \n")
    nfile.write("Leetcodes Left: " + str(count) + "\n")

    for i in range(len(comparison_file)):
        if i != len(comparison_file) - 1 and comparison_file[i] not in new_file:
            nfile.write(comparison_file[i] + '\n')
        elif i == len(comparison_file) - 1 and comparison_file[i] not in new_file:
            nfile.write(comparison_file[i])
