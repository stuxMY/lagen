# LAGEN - LAZY PASSWORD GENERATOR 🛠️

**LAGEN** (Lazy Password Generator) is a Python script that helps users generate secure, customizable passwords with ease. This all-in-one tool includes features for generating single or bulk passwords, hashing, encoding, and exporting passwords to files and emails.
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

   git clone https://github.com/yourusername/LAGEN-LazyPasswordGenerator.git
   cd LAGEN-LazyPasswordGenerator
    Ensure Python 3 is installed on your system.

    Run the script, which will check for missing dependencies and install them if necessary.

Usage

Run the script using:

python3 lagen.py

Follow the on-screen menu for available options:

    Generate a single password for a username
    Generate bulk passwords for a list of usernames
    Generate a single password without a username
    Generate bulk passwords without usernames
    MD5 hash a string
    Decode Base64 text
    Generate a JWT token
    Export generated content to PDF
    Send results via email
    Exit

Sample Commands

    Single Password Generation
        Enter username and customize the password parameters (length, uppercase, lowercase, numbers, special characters).

    Bulk Password Generation
        Choose between manual username entry or file input, and customize password parameters.

    Exporting
        Use option 8 to export generated content as a PDF file.

    Sending Email
        Send results via email with an optional PDF attachment using option 9.

Example

To generate and export bulk passwords for a list of usernames:

    Choose option 2 in the menu.
    Enter usernames manually or load from usernames.txt.
    Customize password length and character types.
    Choose option y to save, enter filename, and select PDF option if needed.
