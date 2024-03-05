"""
832. Flipping an Image

Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 
Constraints:

n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.
"""
def flip_and_invert_image(image : list[list[int]]) -> list[list[int]]:

    lst = []

    for row in image:
        row.reverse()

    for row in image:
        temp = []
        for i in row:
            if i == 0:
                temp.append(1)
            else:
                temp.append(0)
        lst.append(temp)
    
    image.clear()
    image += lst

    return image  

def main():
    # print(flip_and_invert_image(image = [[1,1,0],[1,0,1],[0,0,0]]))
    print(flip_and_invert_image(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

if __name__ == "__main__":
    main()