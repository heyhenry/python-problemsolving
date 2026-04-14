"""
4. Matching songs
We have a database of songs, and now we want to find all songs that have the given letters in them in order.
So if we have the letters ac, then we would get "American Pie", but not "Decades".
File format: a request order (any number of lowercase letters in order), followed by an alphabetical list of
names in the song database (which can be any letter, space, or number).
Output: a list of songs in alphabetical order that match the given request order
Note that capitalization doesn't matter, so a matches both A and a
"""
def matches_found(filename : str) -> list[str]:
    with open(filename, "r") as file:
        # place file info into content's variable as a single string element in a list
        content = file.read()
        # turn content into a list of lists with each list being for each line
        content = content.splitlines()
        # create a variable that houses the filter letters
        filter = content[0]
        # remove the first element (the filter letters) from the list of searchable songs
        content.remove(content[0])
        # filtering songs based on given filter and rules
        matched_songs = []
        for song in content:
            temp = list(filter)
            for letter in song.lower():
                if temp and letter == temp[0]:
                    temp.pop(0)
            if len(temp) == 0:
                matched_songs.append(song)
        # returns results
        return matched_songs

test_cases = [
    "test_cases/4/input1.txt",
    "test_cases/4/input2.txt",
    "test_cases/4/input3.txt"
]

for test in test_cases:
    print(matches_found(test))

