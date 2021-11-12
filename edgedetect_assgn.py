from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = r"C:\Github_repository\Edge_detection_python\images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to gracescale and returns the gracescale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
new_pixel_values = [[0 for i in range(numb_colns)] for j in range(numb_rows)]
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1,0,1), (-2,0,2), (-1,0,1))

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(arr,k,l):
    lst1 = [i [l-1:l+2] for i in arr[k-1:k+2]]
    return lst1

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(lst):
    final_list=[j for i in lst for j in i]
    return final_list

for i in range(1,numb_rows+1):
    for j in range(1,numb_colns+1):
# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 bok using list slicing
        neighbour_pixels = get_slice_2d_list(pixel_values,i,j)
    # Appll the mask
    # Sum all the multiplied values and set the new pixel value
        lst2 = sum(list(map(lambda q,w : q*w, flatten(neighbour_pixels), flatten(mask))))
        new_pixel_values[i-1][j-1] = lst2
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify Your final_result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)