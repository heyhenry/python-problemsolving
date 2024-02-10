def matching_songs(filename : str):

    results = []

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            songs = read_content.splitlines()

            filter = []
            
            for c in songs[0]:
                filter.append(c)
            
            stack = []

            for song in range(1, len(songs)):           
                if len(stack) != len(filter):
                    stack.clear()
                    stack += filter
                for c in songs[song].lower():
                    if len(stack) == 0:
                        break
                    elif len(stack) > 0 and c == stack[0]:
                        stack.pop(0)
                    elif len(stack) > 0 and c in filter and c == filter[0]:
                        stack.clear()
                        stack += filter
                        stack.pop(0)
                    elif len(stack) > 0 and c in filter and c != stack[0]:
                        stack.clear()
                        stack += filter
                if len(stack) == 0:
                    results.append(songs[song])
                        
    return results

def main():
    print(matching_songs('4/input1.txt'))
    print(matching_songs('4/input2.txt'))
    print(matching_songs('4/input3.txt'))

if __name__ == "__main__":
    main()