import json
from difflib import get_close_matches
import sys

data = json.load(open("/your_file_path/data.json"));

def diction(x):
    x = x.lower();
    if x in data:
        return data[x];
    elif x.title() in data:
        return data[x.title()];
    elif x.upper() in data:
        return data[x.upper()];
    elif len(get_close_matches(x, data.keys())) > 0:
        return "The word could not be found. Perhaps you meant to enter '%s'?" % get_close_matches(x, data.keys())[0];
    else:
        return "The word could not found and there were no close matches. Please double check it.";


entry = sys.argv
del entry[0]


if len(entry) < 1:
    print("Please provide a word as an argument.");
else:
    word = ' '.join(entry)
    word = word[1:-1]
    output = diction(word)
    if type(output) == list:
        for item in output:
            print(item);
    else:
        print(output)
    

