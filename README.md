# Secret Scanner

A simple Python script to scan a directory recursively for common AWS secrets (access keys, secret keys, session tokens) in files.

## Features

- Recursively scans all files in a specified directory  
- Ignores common binary file types and specific directories (e.g., `.git`, `venv`, `node_modules`) to speed up scanning  
- Detects AWS Access Keys, AWS Secret Access Keys, and AWS Session Tokens using regex patterns  
- Prints any detected secrets with file locations  
- Returns exit code 1 if any secrets are found, otherwise 0  

## Usage

1. Clone the repository or download the script

2. Run the script with the target directory as an argument:

```bash
python3 scan_for_secrets.py /path/to/your/codebase
