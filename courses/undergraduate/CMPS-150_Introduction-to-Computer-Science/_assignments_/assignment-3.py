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
# Define cake types.
cake_types:     list =  ["Cinnamon", "Blueberry", "Bavarian"]

# Initialize order entry.
order_entry:    dict =  {
                            cake_type:      {
                                                "large":    {
                                                                "quantity": 0,
                                                                "cost":     0.0
                                                            },
                                                "small":    {
                                                                "quantity": 0,
                                                                "cost":     0.0
                                                            },
                                                "total":    {
                                                                "quantity": 0,
                                                                "cost":     0.0
                                                            }
                                            }
                            for cake_type in cake_types
                        }

# Initialize receipt.
receipt:    str =   f"""
==============================================
               HAPPY MARDI GRAS                 
==============================================

{"King Cake":15}{"Large":>10}{"Small":>10}{"Cost":>10}
----------------------------------------------
"""

# For each type of cake...
for cake_type in order_entry.keys():
    
    # Prompt for the number of cakes.
    order_entry[cake_type]["total"].update(
        {"quantity": int(input(f"\nHow many {cake_type} cakes would you like? "))}
    )
    
    # If the number of cakes is greater than zero...
    if order_entry[cake_type]["total"]["quantity"] > 0:
        
        # Add cake type to receipt.
        receipt +=  f"""\n{cake_type:15}"""
        
        # Prompt for the nuymber that should be large cakes.
        order_entry[cake_type]["large"].update(
                                                {
                                                    "quantity": int(input(f"And how many of those should be large?   "))
                                                }
                                            )
        
        # Add large quantity to receipt.
        receipt +=  f"""{order_entry[cake_type]["large"]["quantity"]:>10}"""
        
        # Calculate small cake quantity.
        order_entry[cake_type]["small"].update(
                                                {
                                                    "quantity": order_entry[cake_type]["total"]["quantity"] - order_entry[cake_type]["large"]["quantity"]
                                                }
                                            )
        
        # Add small quantity to receipt.
        receipt +=  f"""{order_entry[cake_type]["small"]["quantity"]:>10}"""
        
        # Calculate large cake costs.
        order_entry[cake_type]["large"].update(
                                                {
                                                    "cost":     (order_entry[cake_type]["large"]["quantity"] * 24.99)
                                                }
                                            )
        
        # Calculate small cake costs.
        order_entry[cake_type]["small"].update(
                                                {
                                                    "cost":     (order_entry[cake_type]["small"]["quantity"] * 16.99)
                                                }
                                            )
        
        # Calculate total costs.
        order_entry[cake_type]["total"].update(
                                                {
                                                    "cost":     (order_entry[cake_type]["large"]["cost"] + order_entry[cake_type]["small"]["cost"])
                                                }
                                            )
        
        # Add total cost for cake type to receipt.
        receipt +=  f"""{f"${round(float(order_entry[cake_type]["total"]["cost"]), 2)}":>10}"""
        
# Add "Total" section to order entry.
order_entry.update(
                            {"Subtotal":    {
                                            "large":    {
                                                            "quantity": 0,
                                                            "cost":     0.0
                                                        },
                                            "small":    {
                                                            "quantity": 0,
                                                            "cost":     0.0
                                                        },
                                            "total":    {
                                                            "quantity": 0,
                                                            "cost":     0.0
                                                        }
                                        }}
                        )

# Add total large cake quantity to receipt.
order_entry["Subtotal"]["large"].update(
                            {
                                "quantity": sum([order_entry[cake_type]["large"]["quantity"] for cake_type in cake_types])
                            }
                        )

# Add total small cake quantity to receipt.
order_entry["Subtotal"]["small"].update(
                            {
                                "quantity": sum([order_entry[cake_type]["small"]["quantity"] for cake_type in cake_types])
                            }
                        )

# Add total cost to receipt.
order_entry["Subtotal"]["total"].update(
                            {
                                "cost":     sum([order_entry[cake_type]["total"]["cost"] for cake_type in cake_types])
                            }
                        )

# Add line before total on receipt.
receipt += "\n=============================================="

# Add "Totals" line to receipt.
receipt +=  f"""\n{"Subtotal":15}{order_entry["Subtotal"]["large"]["quantity"]:>10}{order_entry["Subtotal"]["small"]["quantity"]:>10}{f"${round(float(order_entry["Subtotal"]["total"]["cost"]), 2)}":>10}"""

# Calculate total quantity of cakes.
order_entry["Subtotal"]["total"].update(
                            {
                                "quantity": order_entry["Subtotal"]["large"]["quantity"] + order_entry["Subtotal"]["small"]["quantity"]
                            }
                        )

# Add total cake quantity to receipt.
receipt +=  f"""\nTotal number of king cakes: {order_entry["Subtotal"]["total"]["quantity"]}"""

# If customer ordered more than 7 cakes...
if order_entry["Subtotal"]["total"]["quantity"] > 7:
    
    # They receive a 10% discount.
    order_entry["Subtotal"]["total"].update(
                                            {
                                                "discount": order_entry["Subtotal"]["total"]["cost"] * .1
                                            }
                                        )

    # Add discount to receipt.
    receipt +=  f"""\nTotal number of king cakes: {order_entry["Subtotal"]["total"]["discount"]}"""
    
# Add bottom border of receipt.
receipt += "\n=============================================="

# Print final receipt.
print(receipt)