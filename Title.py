import requests
import re

# URL to scrape
url = "https://www.example.com"

# Fetch the page
response = requests.get(url)
html_content = response.text

# Extract the title using regex
title_pattern = r"<title>(.*?)</title>"
match = re.search(title_pattern, html_content, re.IGNORECASE | re.DOTALL)

if match:
    title = match.group(1).strip()
    print("Page title:", title)
    
    # Save to file
    with open("page_title.txt", "w") as f:
        f.write(f"Page title: {title}\n")
    print("✅ Title saved to page_title.txt")
else:
    print("❌ Could not find the page title.")
