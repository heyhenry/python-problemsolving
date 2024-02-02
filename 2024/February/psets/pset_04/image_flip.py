def img_flip(filename : str):

    with open(filename, 'r') as file:

        new_filename = filename[:filename.rfind('.')] + '.flipped'

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()

            split_lines.reverse()

            with open(new_filename, 'w') as nfile:

                for line in range(len(split_lines)):
                    if line != len(split_lines) - 1:
                        nfile.write(split_lines[line] + '\n')
                    else:
                        nfile.write(split_lines[line])

def main():
    print(img_flip('2/input1.txt'))
    print(img_flip('2/input2.txt'))
    print(img_flip('2/input3.txt'))
    print(img_flip('2/input4.txt'))
    print(img_flip('2/input5.txt'))
    
if __name__ == "__main__":
    main()