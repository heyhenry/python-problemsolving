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
    pass

test_cases = [
    "test_cases/2/input1.txt",
    "test_cases/2/input2.txt",
    "test_cases/2/input3.txt",
    "test_cases/2/input4.txt",
    "test_cases/2/input5.txt"
]

for test in test_cases:
    flip_image(test)
