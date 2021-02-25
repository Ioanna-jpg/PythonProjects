# Python program to convert text
# file to JSON
import json

# the file to be converted to
# json format


filename = open(r"C:\Users\jokir\OneDrive\Υπολογιστής\dictionary.txt")

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(r"C:\Users\jokir\OneDrive\Υπολογιστής\dictionary.txt") as fh:

    for line in fh:

        # reads each line and trims of extra the spaces
        # and gives only the valid words
        command, description = line.strip().split(None, 1)
        dict1[command] = description.strip()

# creating json file
# the JSON file is named as f
out_file = open("f.json", "w")
json.dump(dict1, out_file, indent = 2, sort_keys = False)
out_file.close()







