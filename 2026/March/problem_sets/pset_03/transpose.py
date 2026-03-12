
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
    with open(filename, "r") as f:
        # read/store content of text file
        content = f.read()
        
        # exit function early if content is empty
        if not content:
            return 
        
        # update content data into list of lists with integer values only
        updated_content = []
        for row in content.splitlines():
            temp = []
            for i in row.split(","):
                temp.append(int(i))
            updated_content.append(temp)
        
        # check if row lengths are the same (aka valid matrix)
        for row in updated_content:
            # exit function early if file is formatted as a valid matrix
            if len(row) != len(updated_content[0]):
                return 
            
        # transpose csv's data
        results = []
        for col in range(len(updated_content[0])):
            temp = []
            for row in range(len(updated_content)):
                temp.append(updated_content[row][col])
            results.append(temp)
    
        # write transponsed data to new csv file
        output_filename = filename[:-4]+"_transposed.csv"
        with open(output_filename, "w") as outfile:
            for row in range(len(results)):
                for i in range(len(results[row])):
                    if i != len(results[row])-1:
                        outfile.write(str(results[row][i]) + ",")
                    else:
                        outfile.write(str(results[row][i]))
                if row != len(results)-1:
                    outfile.write("\n")

test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for case in test_cases:
    transpose(case)

