
verhoeff_d_table = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
    (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
    (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
    (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
    (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
    (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
    (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
    (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))

verhoeff_p_table = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
    (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
    (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
    (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
    (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
    (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
    (7, 0, 4, 6, 9, 1, 3, 2, 5, 8))

verhoeff_inv_table = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

def calculate_verhoeff_checksum(number):
    """For a given number, calculates the Verhoeff checksum digit."""
    c = 0
    for i, item in enumerate(reversed(str(number))):
        c = verhoeff_d_table[c][verhoeff_p_table[(i + 1) % 8][int(item)]]
    return verhoeff_inv_table[c]

def validate_verhoeff_checksum(number):
    """Validate Verhoeff checksummed number (checksum is the last digit)."""
    c = 0
    for i, item in enumerate(reversed(str(number))):
        c = verhoeff_d_table[c][verhoeff_p_table[i % 8][int(item)]]
    return c == 0

def verhoeff_check(number):
    """For a given number, returns number with Verhoeff checksum digit appended."""
    return f"{number}{calculate_verhoeff_checksum(number)}"

def validate_data(extracted_data, database):
    """Cross-check extracted Aadhaar details with database."""
    # Example database format: {'Name': 'John Doe', 'DOB': '01-01-1990', 'Gender': 'Male'}
    return all(extracted_data[key] == database[key] for key in extracted_data if key in database)

def debug_verhoeff_calculation(number):
    """Print the intermediate OCR values used in the Verhoeff checksum calculation."""
    c = 0
    print("Intermediate OCR values:")
    for i, item in enumerate(reversed(str(number))):
        prev_c = c
        c = verhoeff_d_table[c][verhoeff_p_table[i % 8][int(item)]]
        print(f"Step {i + 1}: Input Digit={item}, Prev Checksum={prev_c}, New Checksum={c}")
    print(f"Final checksum value: {c}")

import re

def validate_pan(pan_number):
    """Validate the PAN card number using a regular expression."""
    pan_pattern = r'^[A-Za-z]{5}[0-9]{4}[A-Za-z]$'
    return bool(re.match(pan_pattern, pan_number))
def validate_dl(dl_number):
    
    dl_pattern = r'\b[A-Z]{2}[0-9]{2}\s?\d{10,12}\b'
    return bool(re.match(dl_pattern, dl_number))
