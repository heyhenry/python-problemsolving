"""
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

    file_index = filename.rfind('.')
    new_filename = filename[:file_index+1] + "solution"

    with open(filename, 'r') as file:
        
        read_content = file.read()
        
        if read_content:

            store_lines = read_content.splitlines()
            content = []

            for row in store_lines:
                temp = []
                for i in row.split(' '):
                    temp.append(i)
                content.append(temp)
            
            reverse_content = []
            reverse_content += content
            reverse_content.reverse()

            with open(new_filename, 'w') as nfile:

                for row in reverse_content:
                    for i in range(len(row)):
                        if i != (len(row)-1):
                            nfile.write(row[i] + ' ')
                        else:
                            nfile.write(row[i])
                    nfile.write("\n")

def main():
    print(image_flip(sys.argv[1]))

if __name__ == "__main__":
    main()