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

    with open(filename, 'r') as file:
        read_content = file.read()
        
        if read_content:
            split_content = read_content.splitlines()
            content = []
            # for row in split_content:
            #     content.append(row.split(' '))
            for row in split_content:
                content.append(row.split(' '))

            revised_content = []

            # up and down flip 
            for row in content:
                row.reverse()
                revised_content.append(row)

            # # side to side flip
            # for row in range(len(content)):
            #     revised_content.append(content[row-1])

            # print(revised_content)

            with open('q2_data/test.output', 'w') as nfile:
                
                for row in revised_content:
                    for i in range(len(row)):
                        if i != len(row) - 1:
                            nfile.write(row[i])
                            nfile.write(' ')
                        else:
                            nfile.write(row[i])
                            nfile.write('\n')
                    
def main():
    # print(flip_image("q2_data/input1.txt")) # passing
    # print(flip_image("q2_data/input2.txt")) # passing
    # print(flip_image("q2_data/input3.txt")) # passing
    # print(flip_image("q2_data/input4.txt")) # passing
    print(flip_image("q2_data/input5.txt")) # wip

# note to self: 
# I have tried the side to side flip as I checked the first and last lines and replicated that, 
# however the digits for the lines in between do not follow the same principle logic, 
# this makes me think maybe there is more to it or it may be an error on the given output file for testcase 5. 
# Either way, if I were to incorporate the side to side flip logic, it would make my first 4 test cases invalid. 
# The current up and down (upside down) logic code seems to suffice imo in regards to the given guidelines but will investigate further.

if __name__ == "__main__":
    main()