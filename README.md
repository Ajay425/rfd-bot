# RedFlagDeals Monitor

This script monitors the RedFlagDeals hot deals forum and detects new deals as they are posted. The script checks the forum at regular intervals and prints out any new deals that have not been seen before.

## Features

- **Frequent Monitoring:** The script checks the RedFlagDeals hot deals forum every minute to ensure that new deals are detected promptly.
- **Deal Detection:** Only new deals that haven't been seen before are printed to the console.
- **Logging:** The script includes logging to track the number of deals found, new deals detected, and any errors that occur during execution.
- **Error Handling:** Robust error handling ensures that the script continues running even if a network or parsing error occurs.

## Prerequisites

- **Python 3.x** is required to run this script.
- The following Python packages are required:
  - `requests`
  - `beautifulsoup4`

You can install the required packages using `pip`:

```bash
pip install requests beautifulsoup4
 
