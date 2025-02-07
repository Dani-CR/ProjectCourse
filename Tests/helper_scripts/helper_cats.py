import os
import json
import re
import sys
from collections import defaultdict

def extract_dict_resultReason(directory):
    dict_rr = defaultdict(int)
    tot = defaultdict(int)
    # Get all JSON files starting with "Test"
    for file in os.listdir(directory):
        if file.startswith("Test") and file.endswith(".json"):
            with open(os.path.join(directory,file), "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Check if "result" is "error"
            if data.get("result") != "error":
                continue
            tot[0] += 1
            if data.get("contractPath") == "/error":
                dict_rr["/error"] += 1
                continue
            reason = data.get("resultReason")
            dict_rr[reason] += 1
    return dict_rr, tot

def refine_dict(raw_dict):
    final_dictionary = defaultdict(int)
    
    for key,value in raw_dict.items():
        if key == "/error":
            final_dictionary[key] = value
            continue
        if key == "Not found":
            final_dictionary["404"] = value
            continue
        match = re.search(r':\s(\d{3})', key)
        insert_key = match.group(1) if match else "000"
        final_dictionary[insert_key] += value
    return final_dictionary

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Error: Provided path is not a directory.")
        sys.exit(1)
        
    
    dict_raw, tot_errors = extract_dict_resultReason(directory)
    print("Evaluated #tests errors: ", tot_errors[0])
    print("\n---Print raw dictionary---------------------------")
    for key in sorted(dict_raw.keys()):
        print(key," = " ,dict_raw[key])
        
    print("\n---Print refined dictionary-----------------------")
    dict_refined = refine_dict(dict_raw)
    for key in sorted(dict_refined.keys()):
        print("Response code ",key, " = ",dict_refined[key])
    
    tot_raw = sum(dict_raw.values())
    tot_refined = sum(dict_refined.values())
    print("FLAG: ", tot_raw==tot_refined)
    #print(dict_rr)
