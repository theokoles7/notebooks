"""
Author:                         Gabriel C. Trahan
ULID:                           C000580009
Course/Section:                 CMPS 150 - Lecture Section #004
Assignment:                     pa2
Date Assigned:                  Tuesday, 03 February, 2020
Date/Time Due:                  Saturday, 08 February, 2020 -- 11:55 pm

Description:                    Determine the amount of paint needed to paint a room.
                
Certification of Authenticity:  I certify that this assignment is entirely my own work.
"""
from math   import ceil

# Ask for the length of the room.
room_length:            float = float(input(f"Enter the length of the room: "))

# Ask for the width of the room.
room_width:             float = float(input(f"Enter the width of the room:  "))

# Ask for the heigh (ceiling height) of the room.
room_height:            float = float(input(f"Enter the height of the room: "))

# Ask for the number of windows in the room.
room_windows:           int =   int(input(f"Enter the number of windows:  "))

# Ask for the number of doorways in the room.
room_doors:             int =   int(input(f"Enter the number of doors:    "))

# Compute the total area of the walls
total_wall_area:        float = ((2 * room_length * room_height) + (2 * room_width * room_height))

# Compute the total window area
# (Every window is 3 x 3)
total_window_area:      float = 3 * 3 * room_windows

# Compute the total door aread
# (Every door is 2.5 x 7)
total_door_area:        float = 2.5 * 7 * room_doors

# Compute the total square footage to paint. (4 walls minus door & windows)
total_sqaure_footage:   float = total_wall_area - total_window_area - total_door_area

# Compute the gallons of paint needed to paint the room.
# (The paint being used covers 315 swuare feet per gallon)
exact_paint_needed:     float = total_sqaure_footage / 315

# Compute the gallons of paint that must be purchased to paint the room.
gallons_paint_needed:   int =   ceil(exact_paint_needed)

# Compute the cost to paint the room.
# (The paint being used costs $27.99 per gallon)
total_cost:             float = 27.99 * gallons_paint_needed

# Print output/results similar to the sample output.
print(f"""
-------------------------------------
     FANCY EARL'S PAINT SERVICE
-------------------------------------

Total Area:                 {round(total_wall_area, 1)}
Window Area:                {round(total_window_area, 1)}
Doorway Area:               {round(total_door_area, 1)}
Square Footage to Paint:    {round(total_sqaure_footage, 1)}

Paint Needed:               {round(exact_paint_needed, 2)} gallons
Paint to Buy:               {round(gallons_paint_needed, 2)} gallons

Cost of Paint:              {round(total_cost, 2)}
""")