# written by James Carvell in python 3.6
# to be run from a terminal
# takes user height in inches and weight in pounds
# uses linear interpolation and bmi tables from below link to find bmi
# https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_tbl.htm
# outputs user bmi and category

# exit used to terminate script if user height or weight are outside of table
from sys import exit

# linear interpolation function
def lin_int(x, x0, x1, y0, y1):
    return(round(y0 + (x - x0) * (y1 - y0) / (x1 - x0), 1))

# reusable strings
how_much = ("""
How {} are you, rounded to the nearest {}?
> """)
sorry = ("""
I'm sorry, but the table this script calculates from can't calculate to that
{}. Have a good day!
""")
try_again = ("""
Please rerun the script and try typing that again with only number characters.
""")

# bmi table from link on line 5
bmi_table = {
58: {91: 19, 96: 20, 100: 21, 105: 22, 110: 23, 115: 24, 119: 25, 124: 26, 129:
27, 134: 28, 138: 29, 143: 30, 148: 31, 153: 32, 158: 33, 162: 34, 167: 35,},
59: {94: 19, 99: 20, 104: 21, 109: 22, 114: 23, 119: 24, 124: 25, 128: 26, 133:
27, 138: 28, 143: 29, 148: 30, 153: 31, 158: 32, 163: 33, 168: 34, 173: 35,},
60: {97: 19, 102: 20, 107: 21, 112: 22, 118: 23, 123: 24, 128: 25, 133: 26, 138:
27, 143: 28, 148: 29, 153: 30, 158: 31, 163: 32, 168: 33, 174: 34, 179: 35,},
61: {100: 19, 106: 20, 111: 21, 116: 22, 122: 23, 127: 24, 132: 25, 137: 26, 143:
27, 148: 28, 153: 29, 158: 30, 164: 31, 169: 32, 174: 33, 180: 34, 185: 35,},
62: {104: 19, 109: 20, 115: 21, 120: 22, 126: 23, 131: 24, 136: 25, 142: 26, 147:
27, 153: 28, 158: 29, 164: 30, 169: 31, 175: 32, 180: 33, 186: 34, 191: 35,},
63: {107: 19, 113: 20, 118: 21, 124: 22, 130: 23, 135: 24, 141: 25, 146: 26, 152:
27, 158: 28, 163: 29, 169: 30, 175: 31, 180: 32, 186: 33, 191: 34, 197: 35,},
64: {110: 19, 116: 20, 122: 21, 128: 22, 134: 23, 140: 24, 145: 25, 151: 26, 157:
27, 163: 28, 169: 29, 174: 30, 180: 31, 186: 32, 192: 33, 197: 34, 204: 35,},
65: {114: 19, 120: 20, 126: 21, 132: 22, 138: 23, 144: 24, 150: 25, 156: 26, 162:
27, 168: 28, 174: 29, 180: 30, 186: 31, 192: 32, 198: 33, 204: 34, 210: 35,},
66: {118: 19, 124: 20, 130: 21, 136: 22, 142: 23, 148: 24, 155: 25, 161: 26, 167:
27, 173: 28, 179: 29, 186: 30, 192: 31, 198: 32, 204: 33, 210: 34, 216: 35,},
67: {121: 19, 127: 20, 134: 21, 140: 22, 146: 23, 153: 24, 159: 25, 166: 26, 172:
27, 178: 28, 185: 29, 191: 30, 198: 31, 204: 32, 211: 33, 217: 34, 223: 35,},
68: {125: 19, 131: 20, 138: 21, 144: 22, 151: 23, 158: 24, 164: 25, 171: 26, 177:
27, 184: 28, 190: 29, 197: 30, 203: 31, 210: 32, 216: 33, 223: 34, 230: 35,},
69: {128: 19, 135: 20, 142: 21, 149: 22, 155: 23, 162: 24, 169: 25, 176: 26, 182:
27, 189: 28, 196: 29, 203: 30, 209: 31, 216: 32, 223: 33, 230: 34, 236: 35,},
70: {132: 19, 139: 20, 146: 21, 153: 22, 160: 23, 167: 24, 174: 25, 181: 26, 188:
27, 195: 28, 202: 29, 209: 30, 216: 31, 222: 32, 229: 33, 236: 34, 243: 35,},
71: {136: 19, 143: 20, 150: 21, 157: 22, 165: 23, 172: 24, 179: 25, 186: 26, 193:
27, 200: 28, 208: 29, 215: 30, 222: 31, 229: 32, 236: 33, 243: 34, 250: 35,},
72: {140: 19, 147: 20, 154: 21, 162: 22, 169: 23, 177: 24, 184: 25, 191: 26, 199:
27, 206: 28, 213: 29, 221: 30, 228: 31, 235: 32, 242: 33, 250: 34, 258: 35,},
73: {144: 19, 151: 20, 159: 21, 166: 22, 174: 23, 182: 24, 189: 25, 197: 26, 204:
27, 212: 28, 219: 29, 227: 30, 235: 31, 242: 32, 250: 33, 257: 34, 265: 35,},
74: {148: 19, 155: 20, 163: 21, 171: 22, 179: 23, 186: 24, 194: 25, 202: 26, 210:
27, 218: 28, 225: 29, 233: 30, 241: 31, 249: 32, 256: 33, 264: 34, 272: 35,},
75: {152: 19, 160: 20, 168: 21, 176: 22, 184: 23, 192: 24, 200: 25, 208: 26, 216:
27, 224: 28, 232: 29, 240: 30, 248: 31, 256: 32, 264: 33, 272: 34, 279: 35,},
76: {156: 19, 164: 20, 172: 21, 180: 22, 189: 23, 197: 24, 205: 25, 213: 26, 221:
27, 230: 28, 238: 29, 246: 30, 254: 31, 263: 32, 271: 33, 279: 34, 287: 35,},
}

# taking user height and checking if within table
try:
    height = int(round(float(input(how_much.format("tall", "inch")))))
except:
    print(try_again)
    exit()
if ((height > 76) or (height < 58)):
    print(sorry.format("height"))
    exit()

# find correct height dictionary, and create list of the weight values
# the dictionary, and variables for the ends of the list 
height_dict = bmi_table.get(height)
height_dict_keys = list(height_dict.keys())
height_dict_keys.sort()
key_count = len(height_dict_keys)
bottom_weight = height_dict_keys[0]
top_weight = height_dict_keys[key_count-1]

# taking user weight, checking if within table, and calculating if between keys
try:
    weight = int(round(float(input(how_much.format("heavy", "pound")))))
except:
    print(try_again)
    exit()

if ((weight > top_weight) or (weight < bottom_weight)):
    print(sorry.format("weight"))
    exit()
elif weight in height_dict_keys:
    bmi = height_dict.get(weight)
else:
    height_dict_keys.append(weight)
    height_dict_keys.sort()
    high_weight_index = height_dict_keys.index(weight)
    height_dict_keys.remove(weight)
    high_weight = height_dict_keys[high_weight_index]
    low_weight = height_dict_keys[high_weight_index-1]
    high_bmi = height_dict.get(high_weight)
    low_bmi = height_dict.get(low_weight)
    bmi = lin_int(weight, low_weight, high_weight, low_bmi, high_bmi)

# determine BMI category
if (bmi < 18.5):
    bmi_cat = "underweight"
elif (bmi < 25):
    bmi_cat = "ideal"
elif (bmi < 30):
    bmi_cat = "overweight"
elif (bmi < 35):
    bmi_cat = "class I obesity"
else:
    bmi_cat = "class II obesity"

# print bmi and category
print(f"\nYour BMI is {bmi}, which is classified as {bmi_cat}")
