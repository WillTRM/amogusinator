from PIL import Image
import numpy as np
import sys
np.set_printoptions(threshold=np.inf)

#if image has factors 4 and 5, amogus army will fit perfectly
print(sys.argv[1:][0])

pixels = np.array(Image.open(sys.argv[1:][0]))
dimensions = pixels.shape
#print(dimensions[0])

def get_average_color(segment_flat):
    r, g, b, pxcount = 0, 0, 0, 0
    for pixel in segment_flat:
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]
        pxcount += 1
    r = r / pxcount
    g = g / pxcount
    b = b / pxcount
    if len(segment_flat[0]) == 4:
        return [r, g, b, 255]
    if len(segment_flat[0]) == 3:
        return [r, g, b]

def generate_amogus(segment, base_color):
    #index 0 = row, index 1 = column
    segment[0][1] = base_color
    segment[0][2] = base_color
    segment[0][3] = base_color

    segment[1][0] = base_color
    segment[1][1] = base_color
    if len(segment[1][1]) == 4:
        segment[1][2] = [255, 255, 255, 255]
        segment[1][3] = [255, 255, 255, 255]
    if len(segment[1][1]) == 3:
        segment[1][2] = [255, 255, 255]
        segment[1][3] = [255, 255, 255]

    segment[2][0] = base_color
    segment[2][1] = base_color
    segment[2][2] = base_color
    segment[2][3] = base_color

    segment[3][1] = base_color
    segment[3][2] = base_color
    segment[3][3] = base_color

    segment[4][1] = base_color
    segment[4][3] = base_color
    
    return segment

top_left_row = 0
top_left_col = 0
bottom_right_row = 0
bottom_right_col = 0

#square should scan a 4 wide, 5 high area
for row in range(0, dimensions[0], 5):
    for col in range(0, dimensions[1], 4):
        top_left_row = row
        top_left_col = col
        bottom_right_row = row + 5
        bottom_right_col = col + 4

        square = pixels[top_left_row:bottom_right_row+1, top_left_col:bottom_right_col+1]
        square_flat = square.reshape(-1, square.shape[-1])
        
        try:
            pixels[top_left_row:bottom_right_row+1, top_left_col:bottom_right_col+1] = generate_amogus(square, get_average_color(square_flat))
        except:
            print("oob lol")
            continue

new_image = Image.fromarray(pixels)
new_image.save("amogusized.png")
