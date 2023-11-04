"""
Returns the sum of each row in the given `.csv` file
Requires that filename ends with `.csv`
Also requires that the given CSV file consist of only integers
Examples:
row_sum("data1.csv") -> []
row_sum("data2.csv") -> [4, 5]
row_sum("data3.csv") -> [-2, -4, 18]
row_sum("data4.csv") -> [6, 9, 12, 15]
"""
def row_sum(filename : str) -> list[int]:

    desired_ext = ".csv"
    given_ext = filename[-4:]

    if given_ext == desired_ext:
        with open(filename, 'r') as file:
            read_content = file.read()
            results = []

            if read_content:

                contents = read_content.splitlines()
        
                for row in contents:           
                    sum_val = 0 
                    for i in row.split(','):
                        sum_val += int(i)
                    results.append(sum_val)
            
        return results

def main():
    print(row_sum("data/data1.csv"))
    print(row_sum("data/data2.csv"))
    print(row_sum("data/data3.csv"))
    print(row_sum("data/data4.csv"))

if __name__ == "__main__":
    main()