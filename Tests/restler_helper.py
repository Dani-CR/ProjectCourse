

    ###################################à
import re
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
            # First match the date part
            if response_pattern.match(line):
                # Remove the timestamp from the matched line
                line_without_timestamp = re.sub(timestamp_removal_pattern, '', line).strip()
                
                # Take the first 26 characters of the response
                response_first_26 = line_without_timestamp[:26]
                
                # Add the first 26 characters to the response_counts list
                response_counts.append(response_first_26)
                
                collect_next = False
    
    # Count occurrences of each unique response
    response_frequency = Counter(response_counts)
    
    # Separate responses containing "HTTP/1.1" and sum the rest as "other"
    filtered_responses = {}
    other_count = 0

    for response, count in response_frequency.items():
        if "HTTP/1.1" in response:
            filtered_responses[response] = count
        else:
            other_count += count

    # Sort responses containing "HTTP/1.1" alphabetically
    sorted_response_frequency = sorted(filtered_responses.items())

    # Add "other" count if there are non-"HTTP/1.1" responses
    if other_count > 0:
        sorted_response_frequency.append((": Received: other", other_count))
    
    return sorted_response_frequency  # Return the sorted frequency count

if __name__ == "__main__":
    log_file_path = "/home/daniela/Downloads/logs_spring-hotel_restler_5.txt"  # Change this to your log file path
    #log_file_path = "/home/daniela/Downloads/logs_spring-hotel_restler_10.txt"

    #log_file_path = "/home/daniela/Downloads/logs_cs02_restler_5.txt"  
    #log_file_path = "/home/daniela/Downloads/logs_cs02_restler_10.txt"

    #log_file_path = "/home/daniela/Downloads/logs_cs04_restler_5.txt"  
    #log_file_path = "/home/daniela/Downloads/logs_cs04_restler_10.txt"

    #log_file_path = "/home/daniela/Downloads/logs_cs03_restler_5.txt"  
    #log_file_path = "/home/daniela/Downloads/logs_cs03_restler_10.txt"

    response_frequencies = extract_log_details(log_file_path)
    tot_responses = sum(count for _, count in response_frequencies)
    print(f"Log File: {log_file_path}\n")
    print("Response Frequencies (First 26 Characters):")
    for response, count in response_frequencies:
        print(f"'{response}': {count}")
    
    print(f"\nTotal Responses: {tot_responses}")

