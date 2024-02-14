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
def image_flip(filename : str):

    new_filename = filename[:filename.rfind('.')] + '.output'

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            lines = read_content.splitlines()
            lines.reverse()
            
            with open(new_filename, 'w') as nfile:

                for l in range(len(lines)):
                    if l != len(lines) - 1:
                        nfile.write(lines[l] + '\n')
                    else:
                        nfile.write(lines[l])

def main():
    print(image_flip("2/input1.txt"))
    print(image_flip("2/input2.txt"))
    print(image_flip("2/input3.txt"))
    print(image_flip("2/input4.txt"))
    print(image_flip("2/input5.txt"))

if __name__ == "__main__":
    main()