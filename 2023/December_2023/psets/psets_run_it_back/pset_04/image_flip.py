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
import sys

def image_flip(filename : str):

    flipped_content = []

    new_filename = '_flipped.txt'
    index = filename.rfind('.txt')
    new_filename = filename[:index] + new_filename
    
    with open(filename, 'r') as file:
        
        read_content = file.read()
        
        split_lines = read_content.splitlines()
        content = []
        
        for row in split_lines:
            content.append(row.split(' '))
        
        flipped_content += content
        flipped_content.reverse()

        with open(new_filename, 'w') as nfile:

            for row in range(len(flipped_content)):
                for i in range(len(flipped_content[row])):
                    if i != len(flipped_content[row]) - 1:
                        nfile.write(flipped_content[row][i] + ' ')
                    else:
                        nfile.write(flipped_content[row][i])
                if row != len(flipped_content) - 1:
                    nfile.write('\n')

def main():
    print(image_flip(sys.argv[1]))

if __name__ == "__main__":
    main()