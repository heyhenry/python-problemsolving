from PIL import Image
import PIL

used_image = "imgs/goku_3.jpg"

# rotating an image
# im1 = Image.open(used_image)
# im1 = im1.rotate(67, PIL.Image.NEAREST, expand=1)
# im1.show()

original_img = Image.open("imgs/goku_3.jpg")

vert_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vert_img.save("vert_goku.png")
vert_img.show()

original_img.close()
vert_img.close()
