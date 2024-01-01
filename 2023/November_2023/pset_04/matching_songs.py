"""
4. Matching songs
We have a database of songs, and now we want to find all songs that have the given letters in them in order.
So if we have the letters ac, then we would get "American Pie", but not "Decades".
File format: a request order (any number of lowercase letters in order), followed by an alphabetical list of
names in the song database (which can be any letter, space, or number).
Output: a list of songs in alphabetical order that match the given request order
Note that capitalization doesn't matter, so a matches both A and a
"""
def matched_songs(filename : str):

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            content = read_content.splitlines()
            search_filter = content[0]
            result = []
            content.pop(0)
            
            for song in content:
                word = search_filter
                for i in song:
                    if len(word) > 0 and i.lower() == word[0]:
                        word = word[1:]
                if len(word) == 0:
                    result.append(song)
            
        return result

def main():
    print(matched_songs('q4_data/input1.txt'))
    print(matched_songs('q4_data/input2.txt'))
    print(matched_songs('q4_data/input3.txt'))

if __name__ == "__main__":
    main()