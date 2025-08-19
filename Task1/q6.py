import re

def extract_phone_numbers(text):
    # Regex pattern to match phone numbers starting with +91-
    pattern = r"\+91-\d{10}"
    return re.findall(pattern, text)

# Sample text
sample_text = (
    "For any support regarding our Bangalore office, call us at +91-9876543210 between 9 AM to 6 PM. "
    "If you are located in Mumbai, you can also reach our helpdesk at 9123456789 for urgent assistance. "
    "Additionally, our Delhi branch can be contacted at +91-9988776655 during weekdays."
)

# Extract phone numbers
print(extract_phone_numbers(sample_text))
