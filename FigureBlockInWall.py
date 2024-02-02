# Define the dimensions of the wall in feet
width = 8
height = 8

# Define the dimensions of a cinder block in feet
cinder_block_width = 16 / 12
cinder_block_height = 8 / 12

# Calculate the number of cinder blocks required per square foot
blocks_per_sq_ft = 1 / (cinder_block_width * cinder_block_height)

# Calculate the total wall area in square feet
wall_area = width * height

# Calculate the total number of cinder blocks required
total_blocks = wall_area * blocks_per_sq_ft

# Print the result
print(f"The number of cinder blocks required to build the wall is: {total_blocks:.2f}")
