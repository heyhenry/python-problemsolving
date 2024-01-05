"""
1436. Destination City
Easy
2.1K
95
Companies
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
"""
def destCity(paths: list[list[str]]) -> str:

    cities = []
    destination = ''
    
    for i in range(len(paths[0])):
        temp = []
        for j in range(len(paths)):
            temp.append(paths[j][i])
        cities.append(temp)
        
    start_trips = cities[0]
    end_trips = cities[1]
    
    for i in end_trips:
        if i in start_trips:
            continue
        else:
            destination = i
            
    return destination

def main():
    print(destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])) # Sao Paulo
    print(destCity(paths = [["B","C"],["D","B"],["C","A"]])) # A
    print(destCity(paths = [["A","Z"]])) # Z
    print(destCity(paths = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]])) # wxAscRuzOl
    print(destCity(paths =
[["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]])) # OAxMijOZgW

if __name__ == "__main__":
    main()