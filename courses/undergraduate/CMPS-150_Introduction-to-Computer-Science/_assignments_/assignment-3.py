"""
Author:                         Gabriel C. Trahan
ULID:                           C000580009
Course/Section:                 CMPS 150 - Lecture Section #004
Assignment:                     pa3
Date Assigned:                  Tuesday, 11 February, 2020
Date/Time Due:                  Saturday, 15 February, 2020 -- 11:55 pm

Description:                    Determine the cost of a Mardi Gras order. Order can include 3 types 
                                of king cakes and possibly beads. Output includes a "neat & tidy 
                                table".
                
Certification of Authenticity:  I certify that this assignment is entirely my own work.
"""
# Initialize order entry.
order_entry:    dict =  {
    "Cinnamon":     {
        "quantity": 0,
        "large":    0
    },
    "Blueberry":    {
        "quantity": 0,
        "large":    0
    },
    "Bavarian":     {
        "quantity": 0,
        "large":    0
    }
}

# Initialize receipt.
receipt:    str =   f"""
------------------------------------------------
                HAPPY MARDI GRAS
------------------------------------------------

{"King Cake":10}{"Large":5}{"Small":5}{"Cost":5}
-------------------------------------------------
"""

# For each type of cake...
for cake_type in order_entry.keys():
    
    # Prompt for the number of cakes.
    order_entry[cake_type].update(
        {"quantity": int(input(f"\nHow many {cake_type:9} cakes would you like? "))}
    )
    
    # If the number of cakes is greater than zero...
    if order_entry[cake_type]["quantity"] > 0:
        
        # Prompt for the nuymber that should be large cakes.
        order_entry[cake_type].update(
            {"large": int(input(f"And how many of those should be large?   "))}
        )
        
# Print receipt.
print(f"""
------------------------------------------------
                HAPPY MARDI GRAS
------------------------------------------------

King Cake   Large   Small   Cost
-------------------------------------------------
Cinnamon    
Blueberry   
Bavarian    
-------------------------------------------------
""")
    
print(order_entry)