"""
Given a CSV filename, calculate the mean of each column in the CSV
Requires that filename end with `.csv` and the file contains only integers
Any empty row element is assumed to be 0
Examples:
column_mean("data1.csv") -> []
column_mean("data2.csv") -> [3, -1, .5, 2]
column_mean("data3.csv") -> [3, 1, 0]
column_mean("data4.csv") -> [2.5, 3.5, 4.5]
"""
def column_mean(filename : str) -> list[float]:

    results = []

    with open(filename, 'r') as file:

        read_content = file.read()

        # always account for empty files
        if read_content:

            # create list of lists of integers
            # 1. split lines into respective list (ie. '\n')
            # 2. remove non-integer components (i.e. ',')
            # 3. loop through each new string value in list and convert into int
            # 4. place converted int values into new list of lists
            rows = read_content.splitlines()
            
            lst_of_lsts = []

            for r in rows:
                temp = []
                line = r.split(',')
                for i in line:
                    temp.append(int(i))
                lst_of_lsts.append(temp)

            # find what the length of the largest list (aka row)

            max_col_len = 0

            for i in lst_of_lsts:
                if max_col_len is None:
                    max_col_len = len(i)
                elif len(i) > max_col_len:
                    max_col_len = len(i)

            # make sure each list has an equal amount of columns based on largest list (aka row)
            
            for i in lst_of_lsts:
                while len(i) != max_col_len:
                    i.append(0)

            # calculate the sum_values for each column & calculate the mean values for each column based on sum value

            for col in range(len(lst_of_lsts[0])):
                sum_value = 0
                mean_value = 0
                for row in range(len(lst_of_lsts)):
                    sum_value += lst_of_lsts[row][col]
                mean_value = sum_value / len(lst_of_lsts)
                results.append(mean_value)

            return results
    
        return results

def main():
    print(column_mean("csv_files/data1.csv"))
    print(column_mean("csv_files/data2.csv"))
    print(column_mean("csv_files/data3.csv"))
    print(column_mean("csv_files/data4.csv"))

if __name__ == "__main__":
    main()