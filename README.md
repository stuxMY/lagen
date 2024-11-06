
<div align="center">
    <a href="https://github.com/stuxMY/lagen">
        <img src="https://i.ibb.co/3yy6h8j/Gemini-Generated-Image-wvjbmswvjbmswvjb.jpg" alt="Logo" width="300" height="330">
    </a>
    <h3>LAGEN - LAZY PASSWORD GENERATOR </h3>
</div>

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

# LAGEN - LAZY PASSWORD GENERATOR 🛠️

**LAGEN** (Lazy Password Generator) is a Python script that helps users generate secure, customizable passwords with ease. This all-in-one tool includes features for generating single or bulk passwords, hashing, encoding, and exporting passwords to files and emails.

**IMPORTANT** 
# Gmail 
Please Setup Google Apps Password before use Sent Email functions

# Payloads.json
Create payload.json file if want to use generate JWT TOKEN

   ```python
## Features

- Generate a single password or bulk passwords with customizable parameters
- Export passwords to text files or PDF
- Send generated passwords via email
- Hash strings using MD5
- Decode Base64 text
- Generate JSON Web Tokens (JWT)
- User-friendly CLI with menu-based navigation
- Optional dependency installer for required libraries

## Dependencies

The script installs the required libraries automatically if they're missing. The dependencies include:

- `crypto_tools` - for cryptographic utilities like hashing and JWT
- `colorama` - for colorful CLI output
- `fpdf` - to create PDF documents
- `smtplib` - for sending emails

## Installation

Clone this repository:

   git clone https://github.com/stuxMY/lagen.git
   cd lagen
    Ensure Python 3 is installed on your system.

    Run the script, which will check for missing dependencies and install them if necessary.

Usage
Run the script using:
python3 lagen.py

Follow the on-screen menu for available options:

   1. Generate a single password for a username
   2. Generate bulk passwords for a list of usernames
   3. Generate a single password without a username
   4. Generate bulk passwords without usernames
   5. MD5 hash a string
   6. Decode Base64 text
   7. Generate a JWT token
   8. Export generated content to PDF
   9. Send results via email
   0. Exit

Sample Commands
1. Single Password Generation
   Enter username and customize the password parameters (length, uppercase, lowercase, numbers, special characters).

2. Bulk Password Generation
   Choose between manual username entry or file input, and customize password parameters.

3. Exporting
   Use option 8 to export generated content as a PDF file.

4. Sending Email
   Send results via email with an optional PDF attachment using option 9.

Example
To generate and export bulk passwords for a list of usernames:

    Choose option 2 in the menu.
    Enter usernames manually or load from usernames.txt.
    Customize password length and character types.
    Choose option y to save, enter filename, and select PDF option if needed.
