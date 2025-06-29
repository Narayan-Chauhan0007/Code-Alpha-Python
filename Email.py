import re

# Input and output file paths
input_file = "sample_text.txt"
output_file = "extracted_emails.txt"

# Read input file
with open(input_file, "r") as f:
    text = f.read()

# Extract email addresses using regex
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# Save emails to output file
with open(output_file, "w") as f:
    for email in emails:
        f.write(email + "\n")

print(f"✅ {len(emails)} email addresses extracted and saved to {output_file}.")
