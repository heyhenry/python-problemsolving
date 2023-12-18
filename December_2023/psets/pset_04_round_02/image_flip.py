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

    results = []
    x = filename.rfind('.')
    new_filename = filename[:x+1] + ".solution"

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            # store each line as an element into a list 
            store_lines = read_content.splitlines()

            # store each value in the element as its own element into a list
            # separator being the space between each value
            content = []
            for row in store_lines:
                content.append(row.split(' '))

            # flip the contents upside down with the reverse built-in function
            results += content
            results.reverse()

            with open(new_filename, 'w') as nfile:
        
                for index, line in enumerate(results):
                    # loop through each value for each line
                    for i in range(len(line)):
                        # write to solution file
                        if i != (len(line)-1):
                            nfile.write(line[i] + ' ')
                        else:
                            nfile.write(line[i])
                    # if not final line, then drop to new line for next line that is about to be looped and written
                    if index != len(results)-1:
                        nfile.write('\n')

def main():
    print(image_flip(sys.argv[1]))

if __name__ == "__main__":
    main()