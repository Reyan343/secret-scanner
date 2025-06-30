#!/usr/bin/python3

import os
import sys
import re
import argparse
from datetime import datetime

# fails = []

def check_for_secrets(file, log_file_path=None):
    found_secrets = False
    
    patterns = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Access Key": r"(?i)aws.+['\"][0-9a-zA-Z\/+]{40}['\"]",
    "AWS Session Token": r"(?:[A-Za-z0-9/+=]{16,})?FQoGZXIvYXdz[^\"]+"
    }

    #check to see if file contains any matches
    with open(file) as f:
        content = f.read()
        for label, pattern in patterns.items():
            
            matches = re.findall(pattern, content)
            
            # Output any matches found
            for match in matches:
                    message = f"[{label}] found in {file}: {match}"
                    print(message)
                    if log_file_path:
                        write_log(message, log_file_path)
                    found_secrets = True           

    return found_secrets

# method to write log file for human review
def write_log(message, log_file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file_path, 'a') as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

        
def main():
    # set up arguments to be used 
    parser = argparse.ArgumentParser(description="Secret scanner script")
    parser.add_argument("directory", help="Directory to scan for secrets")
    parser.add_argument("-l", "--log", help="Path to log file", default="secrets.log")
    args = parser.parse_args()

    directory = args.directory
    log_file_path = args.log

    # scan through every file in the directory and output its content
    found_any_secrets = False

    ignore_dirs = {'.git', 'venv', '__pycache__', 'node_modules'} # directories to ignore to speed up search
    ignored_extensions = {'.jpg', '.png', '.pdf', '.zip', '.exe', '.dll', '.so'}


    for root, dirs, files in os.walk(directory):
        # Remove ignored directories from the traversal
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file in files:
            if any(file.lower().endswith(ext) for ext in ignored_extensions):
                continue  # Skip this file if the extension matches the ignore list
            try:
                found = check_for_secrets(os.path.join(root, file), log_file_path=log_file_path)
                if found:
                    found_any_secrets = True
                # print(open(os.path.join(root, file)).read())
            except UnicodeDecodeError:
                print ("Unable to read file: " + os.path.join(root, file))
                # fails.append(os.path.join(root, file)) # comment out when not debugging

    if found_any_secrets:
        print("Secrets found!")
        sys.exit(1)
    else:
        print("No matches found")
        sys.exit(0) 

    # print (fails) # use to check which files are not being read properly

if __name__ == "__main__":
    main()


