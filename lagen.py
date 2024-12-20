#!/usr/bin/env python3
import os
import subprocess
import sys
import configparser
import random
import string
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from fpdf import FPDF
from crypto_tools import md5_hash, base64_decode, generate_jwt_token
from colorama import init, Fore, Back, Style

required_libraries = [
    'crypto_tools',
    'colorama',
    'fpdf',
    'smtplib',
]

def install_missing_libraries(libraries):
    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            print(f"Lib '{lib}' not found. Installing == == > > ")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

install_missing_libraries(required_libraries)

def load_email_credentials():
    config = configparser.ConfigParser()

    if not os.path.exists("email.conf"):
        print("Email configuration file 'email.conf' not found.")
        print("Please create the file 'email.conf' with your email and password.")
        return None, None
    
    config.read('email.conf')
    try:
        email = config.get('smtp', 'email')
        password = config.get('smtp', 'password')
        return email, password
    except Exception as e:
        print(f"Error reading 'email.conf': {e}")
        return None, None

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    characters = ''
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    if not characters:
        raise ValueError("at least one character set (uppercase, lowercase, numbers, special characters) must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def usernames_from_file(filename):
    try:
        with open(filename, 'r') as file:
            usernames = [line.strip() for line in file.readlines()]
        return usernames
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def generate_bulk_passwords(usernames, length=12, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    passwords = {}
    
    for username in usernames:
        try:
            password = generate_password(length, uppercase, lowercase, numbers, special_characters)
            passwords[username] = password
        except ValueError as e:
            passwords[username] = str(e)

    return passwords

def gen_single_password(username, length=12, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    try:
        password = generate_password(length, uppercase, lowercase, numbers, special_characters)
        return {username: password}
    except ValueError as e:
        return {username: str(e)}

def save_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Passwords saved to '{filename}' successfully.")
    except Exception as e:
        print(f"Error saving to file: {str(e)}")

def export_to_pdf(filename, content):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in content.split("\n"):
            pdf.cell(200, 10, txt=line, ln=True, align='L')
        pdf.output(filename)
        print(f"Exported to PDF file '{filename}' successfully.")
    except Exception as e:
        print(f"Error exporting to PDF: {str(e)}")

def send_email(sender_email, recipient_email, subject, content, pdf_filename=None):
    try:
        password = input(f"Enter the password for '{sender_email}': ") if not sender_email or not password else password
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(content, 'plain'))
        
        if pdf_filename:
            with open(pdf_filename, 'rb') as pdf_file:
                part = MIMEApplication(pdf_file.read(), _subtype='pdf')
                part.add_header('Content-Disposition', 'attachment', filename=pdf_filename)
                msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        print(f"Email sent to '{recipient_email}' successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

def menu():
    print("""
🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 ® Free Palestine
██╗      █████╗  ██████╗ ███████╗███╗   ██╗
██║     ██╔══██╗██╔════╝ ██╔════╝████╗  ██║
██║     ███████║██║  ███╗█████╗  ██╔██╗ ██║
██║     ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║
███████╗██║  ██║╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """)
    print("1. Single password with username")
    print("2. Bulk passwords with usernames")
    print("3. Password only")
    print("4. Bulk passwords only")
    print("5. MD5 Hash")
    print("6. Base64 decode")
    print("7. Generate JWT token")
    print("8. Export to PDF")
    print("9. Email the results")
    print("0. Exit")

def main():
    generated_content = ""

    while True:
        menu()
        option = input("Choose (0-9): ")

        if option == '0':
            print("Exit. LOLbye!")
            break

        elif option == '9':
            sender_email, password = load_email_credentials()
            if sender_email is None or password is None:
                continue

            recipient_email = input("Recipient email address: ")
            subject = input("Email subject: ")
            pdf_filename = input("Attach PDF (filename) or leave blank: ")
            send_email(sender_email, recipient_email, subject, generated_content, pdf_filename)

if __name__ == "__main__":
    main()
