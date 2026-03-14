"""
2. Image Flip
(Monochrome) images can be represented as matrices, with numbers between 0 and 255. Your task is to take
such an image and "flip" it so that it's upside down.
File format: a series of lines of space-separated numbers, where each number is between 0 and 255. Each line
will be the same length (the image is rectangular)
Output: a matrix of numbers between 0 and 255, of the same size as the input.
If you're feeling fancy, you can try and visualize these images! Pillow's Image save method can actually write
out images in the format we're using, so you can make a png or whatever of them!
"""
def flip_image(filename : str):
    with open(filename, "r") as file:
        content = file.read()

        # create list of element per line
        content = content.splitlines()
        
        # new soluton's filename
        new_filename = filename[:-4]+".solution"

        # create solution/output file
        with open(new_filename, "w") as outfile:
            counter = -1
            for row in content[::-1]:
                counter += 1
                if counter != len(content)-1:
                    outfile.write(row + "\n")
                else:
                    outfile.write(row)

test_cases = [
    "test_cases/2/input1.txt",
    "test_cases/2/input2.txt",
    "test_cases/2/input3.txt",
    "test_cases/2/input4.txt",
    "test_cases/2/input5.txt"
]

for test in test_cases:
    flip_image(test)
