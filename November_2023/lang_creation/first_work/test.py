filename = 'test_cases/input1.txt'

# find test file name:
a = filename.rfind('/')
# print(print(filename[a+1:]))
temp_filename = filename[a+1:]
target_filename = temp_filename.replace('input', 'solution')
# print(target_filename)

# find directory name:
b = filename.rfind('/')
directory_name = filename[:b+1]
# print(directory_name)
new_filename = directory_name + target_filename
print(new_filename)