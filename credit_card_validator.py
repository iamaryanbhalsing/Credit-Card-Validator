def luhn_algorithm(card_number):
    """
    Validates a credit card number using the Luhn algorithm.
    Returns True if valid, False otherwise.
    """
    # Remove non-digit characters
    digits = [int(d) for d in card_number if d.isdigit()]
    
    if not digits or len(digits) < 13 or len(digits) > 19:
        return False
    
    # Reverse the digits for processing
    digits = digits[::-1]
    
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:  # Every second digit starting from the right (0-based after reverse)
            digit *= 2
            if digit > 9:
                digit -= 9  # or digit = digit // 10 + digit % 10
        total += digit
    
    return total % 10 == 0

def validate_credit_card(card_number):
    """
    Validates and provides basic info about the credit card.
    """
    if not luhn_algorithm(card_number):
        return "Invalid credit card number."
    
    # Basic card type detection
    cleaned = ''.join(d for d in card_number if d.isdigit())
    if cleaned.startswith(('4',)):
        card_type = "Visa"
    elif cleaned.startswith(('51', '52', '53', '54', '55')) or (len(cleaned) == 16 and cleaned[0] == '5'):
        card_type = "Mastercard"
    elif cleaned.startswith(('34', '37')):
        card_type = "American Express"
    elif cleaned.startswith(('6011', '65')) or cleaned.startswith('644') or cleaned.startswith('645') or cleaned.startswith('646') or cleaned.startswith('647') or cleaned.startswith('648') or cleaned.startswith('649'):
        card_type = "Discover"
    else:
        card_type = "Unknown"
    
    return f"Valid {card_type} credit card number."

if __name__ == "__main__":
    print("Credit Card Validator")
    while True:
        num = input("Enter credit card number (or 'quit' to exit): ").strip()
        if num.lower() == 'quit':
            break
        result = validate_credit_card(num)
        print(result)
        print("-" * 40)