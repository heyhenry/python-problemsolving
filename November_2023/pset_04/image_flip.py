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

            for row in split_content:
                content.append(row.split(' '))

            content.reverse()

            new_file = 'q2_data/flipped_output' + filename[13:]

            with open(new_file, 'w') as nfile:
                
                for row in content:
                    for i in range(len(row)):
                        if i != len(row) - 1:
                            nfile.write(row[i])
                            nfile.write(' ')
                        else:
                            nfile.write(row[i])
                            nfile.write('\n')
                    
def main():
    print(flip_image("q2_data/input1.txt")) 
    print(flip_image("q2_data/input2.txt")) 
    print(flip_image("q2_data/input3.txt")) 
    print(flip_image("q2_data/input4.txt")) 
    print(flip_image("q2_data/input5.txt"))

if __name__ == "__main__":
    main()