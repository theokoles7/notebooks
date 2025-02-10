"""
Author:                         Gabriel C. Trahan
ULID:                           C000580009
Course/Section:                 CMPS 150 - Lecture Section #004
Assignment:                     pa1
Date Assigned:                  Monday, 27 January, 2020
Date/Time Due:                  Friday, 31 January, 2020 -- 11:55 pm

Description:                    This program computes all arithmetic operations, given 2 
                                operands. It also prints the operations, operators, and results.
                
Certification of Authenticity:  I certify that this assignment is entirely my own work.
"""

# Ask the user for their name.
username:   str =   input("Enter your name: ")

# Ask the user for operand #1.
operand_1:  int =   int(input("Enter operand #1: "))

# Ask the user for operand #2.
operand_2:  int =   int(input("Enter opernad #2: "))

# Get the length of operand characters.
length_1:   int =   len(str(operand_1))
length_2:   int =   len(str(operand_2))

# Compute and print output similar to the sample output.
print(f"""
--------------------------------------------------------

Your name is: {username}

{operand_1:{length_1}} +  {operand_2:{length_2}} = {operand_1 +     operand_2:15.2f}
{operand_1:{length_1}} -  {operand_2:{length_2}} = {operand_1 -     operand_2:15.2f}
{operand_1:{length_1}} *  {operand_2:{length_2}} = {operand_1 *     operand_2:15.2f}
{operand_1:{length_1}} /  {operand_2:{length_2}} = {operand_1 /     operand_2:15.2f}
{operand_1:{length_1}} // {operand_2:{length_2}} = {operand_1 //    operand_2:15.2f}
{operand_1:{length_1}} %  {operand_2:{length_2}} = {operand_1 %     operand_2:15.2f}
{operand_1:{length_1}} ** {operand_2:{length_2}} = {operand_1 **    operand_2:15.2f}
""")