# https://github.com/asalnorouzzade/Practice-42-Date-Extraction.git
import re
text = input().strip()
pattern_one = r"(?<![0-9])(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])(?![0-9])"
pattern_two = r"(?<![0-9])(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})(?![0-9])"
pattern = f"({pattern_one})|({pattern_two})"
results = re.finditer(pattern, text)
found = False

for result in results:
    found = True
    
    if result.group(1):
        year = result.group(2)
        month = result.group(3)
        day = result.group(4)
        
    else:
        day = result.group(6)
        month = result.group(7)
        year = result.group(8)
        
    print(f"{year}-{month}-{day}")

if not found:
    print("None")
