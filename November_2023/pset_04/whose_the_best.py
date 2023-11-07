"""
3. Who's the best
2 / 2
We wanna figure out who has the best name. Fortunately we have a perfect ordering of names (generated by
a magical AI), and just need a way to understand what it spits out. Then print out the best one!
File format: a series of lines of the form Name1 > Name2
Output: one of three things:
1. if a name is better than all others, then that name
2. if multiple names could be the best, then "UNKNOWN"
3. if there's a contradiction (Name1 > Name2, but Name2 > Name1), then "INVALID"
"""
# def whose_the_best(filename: str):

#     with open(filename, 'r') as file:
#         read_content = file.read()
#         result = ''
#         if read_content:
#             split_list = read_content.splitlines()
#             content = []
#             for row in split_list:
#                 temp = []
#                 for i in row.split(' '):
#                     temp.append(i)
#                 content.append(temp)

#             names = []

#             for row in content: 
#                 for i in row:
#                     if i not in names and i != '<' and i != '>':
#                         names.append(i)

#             name_hierarchy = {}

#             for i in names:
#                 name_hierarchy[i] = []
            
#             for row in content:
#                 if row[1] == '<':
#                     name_hierarchy[row[2]].append(row[0])
#                 elif row[1] == '>':
#                     name_hierarchy[row[0]].append(row[2])

#             # print(name_hierarchy)                
#             best_name = None
#             for key, values in name_hierarchy.items():

#                 if not values:
#                     if best_name is not None:
#                         result = 'Unknown'
#                         break    
#                     best_name = key
            
#             if result != 'Unkown' and best_name is not None:
#                 result = best_name
#             else:
#                 result = 'Invalid'
        
#         return result
def whose_the_best(filename: str):
    def topological_sort(graph):
        in_degree = {name: 0 for name in graph}
        for neighbors in graph.values():
            for neighbor in neighbors:
                in_degree[neighbor] += 1

        queue = [name for name, degree in in_degree.items() if degree == 0]
        result = []

        while queue:
            name = queue.pop(0)
            result.append(name)
            if name in graph:
                for neighbor in graph[name]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        return result

    with open(filename, 'r') as file:
        read_content = file.read()
        result = ''
        if read_content:
            split_list = read_content.splitlines()
            name_hierarchy = {}

            for row in split_list:
                name1, name2 = row.split(" > ")
                if name2 not in name_hierarchy:
                    name_hierarchy[name2] = []
                name_hierarchy[name2].append(name1)

            # Find names with no out-degrees (names without neighbors)
            names_with_no_neighbors = [name for name in name_hierarchy if name not in name_hierarchy[name]]
            
            sorted_names = topological_sort(name_hierarchy)

            # If there are names with no neighbors, add them to the sorted list
            sorted_names += names_with_no_neighbors

            if len(sorted_names) == 1:
                result = sorted_names[0]
            elif len(sorted_names) > 1:
                result = "UNKNOWN"
            else:
                result = "INVALID"

        return result




def main():
    print(whose_the_best('q3_data/input1.txt')) # Alice
    # print(whose_the_best('q3_data/input2.txt')) # Invalid
    # print(whose_the_best('q3_data/input3.txt')) # Unknown
    # print(whose_the_best('q3_data/input4.txt')) # Alice
    # print(whose_the_best('q3_data/input5.txt')) # Elmer
    # print(whose_the_best('q3_data/input6.txt')) # Carol
    # print(whose_the_best('q3_data/input7.txt')) # Invalid

if __name__ == "__main__":
    main()