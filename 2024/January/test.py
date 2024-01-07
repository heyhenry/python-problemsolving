
def decimal_to_binary(num : int):

    a_num = num 
    binary = ''
    while a_num > 1:
        binary += str(int(a_num % 2))
        a_num = int(a_num / 2)
    
    binary += str(a_num)

    while len(binary) < 8:
        binary += '0'

    return binary[::-1]     

def binary_conversion_table(start : int, stop : int):

    results = []

    for i in range(start, stop+1):
        results.append(decimal_to_binary(i))
        
    with open('table.txt', 'w') as file:

        for i in range(len(results)):
            if i != len(results)-1:
                file.write(results[i] + '\n')
            else:
                file.write(results[i])

def main():

    start = int(input('Start: '))
    stop = int(input('Stop: '))
    print(binary_conversion_table(start, stop))

if __name__ == "__main__":
    main()    
