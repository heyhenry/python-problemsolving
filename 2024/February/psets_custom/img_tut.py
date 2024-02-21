from PIL import Image

with open('imgs/input3.solution') as file:
    lines = file.readlines()

img_data = [int(x) for line in lines for x in line if x.isdigit()]

height = len(lines)
width = len(img_data) // height

img = Image.new('P', (width, height), 0)

img.save('test.png')

