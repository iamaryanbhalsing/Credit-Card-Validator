# 🧑‍💻Credit Card Validator

A simple Python script to validate credit card numbers using the **Luhn algorithm**. It checks the structural validity of card numbers and provides basic issuer detection.

---

## ♾️Features
- Validates credit card numbers using the Luhn (Mod-10) checksum algorithm.
- Supports card lengths from 13 to 19 digits.
- Automatically removes spaces, dashes, or other non-digit characters.
- Detects common card types: Visa, Mastercard, American Express, Discover.
- Interactive command-line interface for easy testing.
- Pure Python — no external dependencies.

---

## How to Use

1. Clone or download the repository.
2. Run the script:
   ```bash
   python3 credit_card_validator.py
   ```
3. Enter a credit card number when prompted.
4. Type quit to exit.

---

## Workflow & How It Works
```
The Luhn algorithm is a checksum formula used to validate identification numbers like credit cards. Here's the step-by-step process implemented:

**#Prepare the digits:**
Convert the card number to a list of integers.
Reverse the list (processing starts from the rightmost digit, which is the check digit).

**#Process every second digit (starting from the right, excluding the check digit):**
Double the value of every second digit.
If the doubled value is greater than 9, subtract 9 (equivalent to summing the individual digits, e.g., 12 → 1+2=3).

**#Sum all digits (processed + unprocessed).**
Check divisibility:
If the total sum is divisible by 10 (total % 10 == 0), the number is valid.
Otherwise, it's invalid.


**#This catches most common typing errors (single digit mistakes, adjacent transpositions).**
4. Card Type Detection
After Luhn validation passes, simple prefix matching is used:


Visa: Starts with 4
Mastercard: Starts with 51-55
American Express: Starts with 34 or 37
Discover: Starts with 6011, 65, etc.
Unknown: For other valid formats.


5. Output

Returns a clear message: "Valid [Type] credit card number." or "Invalid credit card number."
```

## Limitations

This tool validates format only — it does not check if the card is active, has sufficient funds, or is legitimate.

For real payment processing, always use official merchant APIs and comply with PCI DSS standards.

---

## Contributing
Feel free to fork and enhance! Ideas: Add more issuers, support for CVV/expiry validation, or a web interface.

---

### 📫 Contact & Socials

<p align="center">
  <a href="mailto:aryanbhalsing7090@gmail.com">
    <img src="https://img.shields.io/badge/Email-aryanbhalsing7090%40gmail.com-red?style=for-the-badge&logo=gmail" />
  </a>
  <a href="https://www.linkedin.com/in/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LinkedIn-iamaryanbhalsing-blue?style=for-the-badge&logo=linkedin" />
  </a>
  <a href="https://github.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/GitHub-iamaryanbhalsing-black?style=for-the-badge&logo=github" />
  </a>
  <a href="https://leetcode.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LeetCode-Profile-orange?style=for-the-badge&logo=leetcode" />
  </a>
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=iamaryanbhalsing&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
</p>

---
<img src="https://camo.githubusercontent.com/a5dbb660f658cb0ba61949a83a2eac3bde636395a476ecc7c16124d2a1f9d8a0/68747470733a2f2f73746174732e70706861742e746f702f69636f6e733f6e616d653d6170706c652c617263686c696e75782c646f636b65722c646a616e676f2c666173746170692c6769746c61622c6769742c6769746875622c6a736f6e2c6a6176617363726970742c6c696e75782c6d6f6e676f64622c6e656f76696d2c6e67696e782c706f737467726573716c2c707974686f6e2c727573742c72656163742c72656469732c7461696c77696e646373732c26636f6c756d6e733d3230" />

---

**Thank you for visiting my profile!** ✨  
Let's build something impactful together.
