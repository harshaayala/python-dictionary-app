
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        word=input("Do you mean %s instead? if yes press Y else N : " % get_close_matches(w, data.keys())[0])
        if word=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif word=="N":
            return "The word is not present"
        else:
            return "we didnt understand your query"
    else:
        return "We could not find the word in the dictionary!"

word=input("Enter Word : ")
output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)