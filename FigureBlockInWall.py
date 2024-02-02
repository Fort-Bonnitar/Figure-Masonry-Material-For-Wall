# Written by Fortbonnitar
# Simple python script to figure materials for a masony built wall

import math

# Define the dimensions of the wall in feet
width = 8
height = 8


def calc_quantity(type_material, wall_size):  #type materals can be either "brick" or "block"
  
  # Define the dimensions of a cinder block in feet
  cinder_block_length = 16  #inches
  cinder_block_height = 8   #inches
  blocks_sq_in = (cinder_block_length * cinder_block_height)
  
  brick_height = 3.625    #inches
  brick_length = 7.625    #inches
  brick_sq_in = (brick_length * brick_height)
  
  # Calculate the total wall area in square feet
  wall_sq_in = (wall_size[0] * wall_size[1]) * 144  # Fix the conversion here
  
  if type_material == 'block':
    total = wall_sq_in / blocks_sq_in
  elif type_material == 'brick':
    total = wall_sq_in / brick_sq_in    
  else:
    print("Error please enter valid material type, only 'brick' or 'block' are valid inputs")
    return
    
  # Print the result
  print(f"The minimum number of {type_material}s required to build the wall is: {math.ceil(total)}")

calc_quantity('block', (width, height))
calc_quantity('brick', (width, height))
