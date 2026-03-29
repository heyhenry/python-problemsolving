
""" 
Given a CSV filename `example.csv`   
If that file is in the form of a matrix (each row has the same length) 
    Writes the transpose of that file to `example_transpose.csv` 
Otherwise, this function does nothing 

A matrix transpose "flips" the matrix over the diagonal: 
    https://en.wikipedia.org/wiki/Transpose 

Examples: 
    transpose("data1.csv") produces an empty file `data1_transpose.csv` 
    transpose("data2.csv") does nothing 
    transpose("data3.csv") produces `data3_transpose.csv` with 
    1,3,5 
    -1,-2,6 
    -2,-5,7 
    transpose("data4.csv") produces `data4_transpose.csv` with 
    1,2,3,4 
    2,3,4,5 
    3,4,5,6 
"""
def transpose(filename : str): 
    
    # formulate output file's naming
    period_index = filename.rfind(".")
    out_filename = filename[:period_index] + "_transpose.csv"

    with open(filename, "r") as file:
        content = file.read()
        
        # if input file is empty, generate defaulted empty output file
        if not content:
            with open(out_filename, "w") as outfile:
                outfile.write("")
            # end the program afterwards
            return

        # turn file content's into list of lists
        content = content.splitlines()
        updated_content = []
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(int(i))
            updated_content.append(temp)
        
        # check if the file contains a valid matrix based on row length comparison
        row_len = len(updated_content[0])
        for row in range(1, len(updated_content)):
            if len(updated_content[row]) != row_len:
                # end the program and do nothing if invalid matrix found
                return
        
        # transpose the file data
        transposed_data = []
        for col in range(len(updated_content[0])):
            temp = []
            for row in range(len(updated_content)):
                temp.append(updated_content[row][col])
            transposed_data.append(temp)

        # write the new transposed data to an output file
        with open(out_filename, "w") as outfile:
            for row in range(len(transposed_data)):
                for i in range(len(transposed_data[row])):
                    if i != len(transposed_data[row]) - 1:
                        outfile.write(str(transposed_data[row][i])+",")
                    else:
                        outfile.write(str(transposed_data[row][i]))
                if row != len(transposed_data) - 1:
                    outfile.write("\n")

test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for case in test_cases:
    print(transpose(case))

