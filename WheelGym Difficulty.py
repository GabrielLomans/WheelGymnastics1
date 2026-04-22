import numpy as np
from flask import Flask 
from markupsafe import escape

# Dictionaries
difficulty = {
    "A": 0.2,
    "B": 0.4,
    "C": 0.6,
    "D": 0.8,
    "E": 1.0
}

structure_group = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "10": "X"
}

# Test Object
#         a,b,c,d,e
number = [0,1,4,4,1]
struct = [1,5,2,8,5,5,5,2,6,8,9,10]

def total_difficulty(number, struct):
    # Initial values
    number_8 = [["A",0],
                ["B",0],
                ["C",0],
                ["D",0],
                ["E",0]
                ]
    difficulty_tot_tech, number_8_tot = 0,0

    # Technical difficulty
    for j in range(len(number)):
        # Counting highest D-values
        i = -1-j
        while number_8[i][1] < number[i]:
            if number_8_tot < 8:
                number_8[i][1] += 1
                number_8_tot += 1
                continue
            else:
                break

        # Calculating total technical difficulty
        difficulty_tot_tech += difficulty[number_8[i][0]] * number_8[i][1]

    # Collecting satisfied structure groups
    struct_sat = []

    for i in range(len(struct)):
        if struct[i] not in struct_sat:
            struct_sat.append(struct[i])
        else:
            continue

    struct_sat_tot = len(struct_sat)
    difficulty_tot_struct = 0.2*struct_sat_tot

    # Total accumulated difficulty
    difficulty_tot = difficulty_tot_tech + difficulty_tot_struct

    # Print
    print("Total difficulty:                %.3f" % difficulty_tot)
    print("Technical difficulty:            %.3f" % difficulty_tot_tech)
    print("Composed of:")
    for i in range(len(number_8)):
        if number_8[i][1] != 0:
            print("         %s x %s" % (number_8[i][1], number_8[i][0]))
    print("Bonus from structure groups:     %.3f" % difficulty_tot_struct)
    print("Satisfied structure groups:")
    for i in range(len(struct_sat)):
        print("         ", structure_group[str(sorted(struct_sat)[i])])
    
    return difficulty_tot, difficulty_tot_tech, difficulty_tot_struct, number_8, struct_sat

print(total_difficulty(number,struct))

