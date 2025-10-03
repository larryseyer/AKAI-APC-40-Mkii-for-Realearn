import sys
import re
import random
import string

def generate_id():
    # Generate 20 random alphanumeric chars (A-Z, a-z, 0-9)
    chars = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    # Insert hyphen at random position (after 1st to 19th char)
    pos = random.randint(1, 19)
    return f'"{chars[:pos]}-{chars[pos:]}"'  # Removed the comma here to place it outside the quotes

if len(sys.argv) != 2:
    print("Usage: python generate_ids.py <input_file>")  # Updated filename suggestion
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.replace('.json', '_output.json')  # Adjust extension if needed

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Match "id": "oldvalue", (with optional spaces around)
        match = re.match(r'(.*"id":\s*)"[^"]*"(.*,\s*.*)', line)
        if match:
            replacement = match.group(1) + generate_id() + match.group(2)
            outfile.write(replacement)
        else:
            outfile.write(line)

print(f"Processed! Output written to {output_file}")
