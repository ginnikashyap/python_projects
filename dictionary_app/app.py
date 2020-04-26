import json
from  difflib import get_close_matches

data = json.load(open("data.json"))

def getdata(word):
    w = word.lower()
    if w in data:
        return (data[word])
    elif len(get_close_matches(w, data.keys()))> 0:
            yn = input("Do you mean %s instead ? Enter Y for yes or N for no: " % get_close_matches(w, data.keys())[0])
            if yn.upper() == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn.upper() == "N":
                return ("This word does not exist")
            else:
                return ("We did not understand your query")

    else:
            return ("This word does not exist")

user_input = input("Enter the key to be searched for ")


output =(getdata(user_input))

if type(output) == list:
    for item in output:
        print(item)

