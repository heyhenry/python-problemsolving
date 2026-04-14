
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
    period_index = filename.rfind(".")
    transposed_filename = f"{filename[:period_index]}_transpose.csv"
    with open(filename, "r") as file:
        content = file.read()
        # create an empty transpose file and end program if input file was empty
        if not content:
            with open(transposed_filename, "w") as outfile:
                outfile.write("")
                return
        content = content.splitlines()
        updated_content = []
        check_row_length = None
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(i)
            # check is rows have same length (i.e same amount of columns), if not - end program without producing transpose file
            if check_row_length is None:
                check_row_length = len(temp)
            elif check_row_length != len(temp):
                return
            updated_content.append(temp)
        transposed_data = []
        for col in range(len(updated_content[0])):
            temp = []
            for row in range(len(updated_content)):
                temp.append(updated_content[row][col])
            transposed_data.append(temp)
        with open(transposed_filename, "w") as outfile:
            for row in range(len(transposed_data)):
                for i in range(len(transposed_data[row])):
                    if i != len(transposed_data[row]) - 1:
                        outfile.write(f"{transposed_data[row][i]},")
                    else:
                        outfile.write(transposed_data[row][i])
                if row != len(transposed_data) - 1:
                    outfile.write("\n")

test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for case in test_cases:
    transpose(case)

