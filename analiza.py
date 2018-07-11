import os
import pandas as pd
import json

num_files = 0
directory = "./gngdata"

logos = ["logos/1.jpg","logos/2.jpg", "logos/3.jpg", "logos/4.jpg"]
results = {"logos/1.jpg":{
                    "correct_ans" : 0,
                    "wrong_ans" : 0,
                    "key_response" : 0},
           "logos/2.jpg":{
                    "correct_ans" : 0,
                    "wrong_ans" : 0,
                    "key_response" : 0,
                },
           "logos/3.jpg":{
                    "correct_ans" : 0,
                    "wrong_ans" : 0,
                    "key_response" : 0,
                },
           "logos/4.jpg":{
                    "correct_ans" : 0,
                    "wrong_ans" : 0,
                    "key_response" : 0,
                }}

def correct_answer(csv, x):
    l = csv["image1"][x]
    if csv["answer"][x] == csv["key_resp_2.keys"][x][2]:
        results[l]["correct_ans"] += 1
    else:
        results[l]["wrong_ans"] += 1

    results[l]["key_response"] += float(csv["key_resp_2.rt"][x][1:17])





for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filename = "gngdata/" + filename
        num_files += 1
        csv = pd.read_csv(filename)
        #print(csv["pix"])
        for x in range(1,len(csv["pix"])):
            s = csv["image1"]
            if s[x] in logos:
                correct_answer(csv,x)

    else:
        pass
for l in logos:
    results[l]["key_response"] /= (num_files*40)

with open('result.json', 'w') as fp:
    json.dump(results, fp)