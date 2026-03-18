import re

n = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(n):
    text = input()
    match = re.findall(pattern, text)

    if not match:
        print("Invalid barcode")
    else:
        barcode = match[0]

        digits = re.findall(r"\d", barcode)

        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")