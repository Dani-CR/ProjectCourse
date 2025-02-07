# python script that given as first argument the network.testing.txt file of the REstlere analysis done gives back the resonses it got
# those responses are kept in a dictionary where key is the type of response and the value is the amount of times that response has been given during the fuzzing 
# if a response has not HTTP/1.1 in the text then it's saved under the "Received: other" key in the dictionary

import re
import argparse
from collections import Counter

def extract_log_details(log_file):
    response_counts = []  # Use a list to store the first 26 characters of each response
    
    sending_pattern = re.compile(r"^\d{4}-\d{2}-\d{2} .*? Sending: '.*?'")
    response_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}")  # Match only YYYY-MM-DD date part
    
    timestamp_removal_pattern = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}")  # To remove full timestamp (including time and milliseconds)
    
    with open(log_file, 'r', encoding='utf-8') as file:
        log_lines = file.readlines()
    
    collect_next = False
    
    for line in log_lines:
        if sending_pattern.match(line):
            collect_next = True
            continue
        
        if collect_next:
            if response_pattern.match(line):
                line_without_timestamp = re.sub(timestamp_removal_pattern, '', line).strip()
                response_first_26 = line_without_timestamp[:26]
                response_counts.append(response_first_26)
                collect_next = False
    
    response_frequency = Counter(response_counts)
    
    filtered_responses = {}
    other_count = 0

    for response, count in response_frequency.items():
        if "HTTP/1.1" in response:
            filtered_responses[response] = count
        else:
            other_count += count

    sorted_response_frequency = sorted(filtered_responses.items())

    if other_count > 0:
        sorted_response_frequency.append((": Received: other", other_count))
    
    return sorted_response_frequency

def main():
    parser = argparse.ArgumentParser(description="Extract and count log responses.")
    parser.add_argument("log_file", help="Path to the log file.")
    args = parser.parse_args()
    
    response_frequencies = extract_log_details(args.log_file)
    tot_responses = sum(count for _, count in response_frequencies)
    
    print(f"Log File: {args.log_file}\n")
    print("Response Frequencies (First 26 Characters):")
    for response, count in response_frequencies:
        print(f"'{response}': {count}")
    
    print(f"\nTotal Responses: {tot_responses}")

if __name__ == "__main__":
    main()

