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
        content = file.read()
        content = content.splitlines()
        
        # the ordered letters to be searched against
        filter = content[0]
        untouched_filter = filter
        
        # find valid songs based on requirements
        skip_first = True
        matched_songs = []
        for song_name in content:
            if skip_first:
                skip_first = False
                continue
            for letter in song_name.lower():
                if len(filter) > 0:
                    if letter == filter[0]:
                        filter = filter[1:]
                if len(filter) == 0:
                    matched_songs.append(song_name)
                    break
            filter = untouched_filter
        return matched_songs

test_cases = [
    "test_cases/4/input1.txt",
    "test_cases/4/input2.txt",
    "test_cases/4/input3.txt"
]

for test in test_cases:
    print(matches_found(test))

