# Secret Scanner

A simple Python script to recursively scan a directory for common AWS secrets (access keys, secret keys, session tokens) in files.

## Features

- Recursively scans all files in a specified directory  
- Ignores common binary file types and specific directories (e.g., `.git`, `venv`, `node_modules`)  
- Detects:
  - AWS Access Keys  
  - AWS Secret Access Keys  
  - AWS Session Tokens  
- Logs findings to a file with timestamps (optional)  
- Prints any detected secrets with file locations  
- Returns exit code `1` if secrets are found, otherwise `0`  

## Usage

1. Clone the repository or download the script.

2. Run the script with the target directory as an argument:

   ```bash
   python3 scan_for_secrets.py /path/to/your/codebase
   ```

3. (Optional) Log the results to a file using the `--log` or `-l` flag:

   ```bash
   python3 scan_for_secrets.py /path/to/your/codebase --log /desired/path/secrets.log
   ```

   If you don’t specify a log file, it defaults to `secrets.log` in the current directory.

   **Example:**

   ```bash
   python3 scan_for_secrets.py ./project_folder -l ./scan_results.log
   ```

## Notes

- Only files with readable text content are scanned. Binary files and unsupported encodings are skipped.
- Common directories and file extensions are excluded to improve performance.
- Log entries include a timestamp for auditing purposes.
