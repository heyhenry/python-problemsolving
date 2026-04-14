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
        filter = content[0]
        content.pop(0)
        results = []
        for song_name in content:
            filter_check = list(filter)
            for c in song_name.lower():
                if filter_check and c == filter_check[0]:
                    filter_check.pop(0)
                elif not filter_check:
                    break
            if not filter_check:
                results.append(song_name)
        return results

test_cases = [
    "test_cases/4/input1.txt",
    "test_cases/4/input2.txt",
    "test_cases/4/input3.txt"
]

for test in test_cases:
    print(matches_found(test))

