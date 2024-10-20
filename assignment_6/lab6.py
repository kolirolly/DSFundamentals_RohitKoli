import numpy as np # type: ignore
depth = 7
rows = 5
cols = 3

# Initialize the 3D array
def initialize(depth, rows, cols):
    arr = np.zeros((depth, rows, cols), dtype=int)
    
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                index_sum = d + r + c
                if (index_sum % 10 == 2) or (index_sum % 10 == 6) :
                    arr[d, r, c] = 0
                else:
                    arr[d, r, c] = 1
    return arr


def longest(arr):                   #longest subarray function
    max_length = 0
    max_coords = []

   
    for d in range(arr.shape[0]):                    # Check rows
        for r in range(arr.shape[1]):
            count = 0
            temp_coords = []
            for c in range(arr.shape[2]):
                if arr[d, r, c] == 1:
                    count += 1
                    temp_coords.append([d, r, c])
                else:
                    if count > max_length:
                        max_length = count
                        max_coords = temp_coords.copy()
                    count = 0
                    temp_coords.clear()
            if count > max_length:
                max_length = count
                max_coords = temp_coords.copy()


    for d in range(arr.shape[0]):                   # Check columns

        for c in range(arr.shape[2]):
            count = 0
            temp_coords = []
            for r in range(arr.shape[1]):
                if arr[d, r, c] == 1:
                    count += 1
                    temp_coords.append([d, r, c])
                else:
                    if count > max_length:
                        max_length = count
                        max_coords = temp_coords.copy()
                    count = 0
                    temp_coords.clear()
            if count > max_length:
                max_length = count
                max_coords = temp_coords.copy()



    for r in range(arr.shape[1]):                       # Check depth (layers)
        for c in range(arr.shape[2]):
            count = 0
            temp_coords = []
            for d in range(arr.shape[0]):
                if arr[d, r, c] == 1:
                    count += 1
                    temp_coords.append([d, r, c])
                else:
                    if count > max_length:
                        max_length = count
                        max_coords = temp_coords.copy()
                    count = 0
                    temp_coords.clear()
            if count > max_length:
                max_length = count
                max_coords = temp_coords.copy()

    return max_length, max_coords

array_3d = initialize(depth, rows, cols)              # Initialize and populate the 3D array


print("Layers:")
for d in range(depth):
    print(f"Layer {d}:")
    for r in range(rows):
        print(array_3d[d, r])
    print("-----")

# printing the longest  block of 1s
longest_block_length, block_start_coords = longest(array_3d)
print(f"\nLength of the largest subarray : {longest_block_length}")
print("\nCoordinates of the largest subarray :\n")
print(block_start_coords)
