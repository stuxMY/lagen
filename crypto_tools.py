import hashlib
import base64
import jwt
import requests
def display_menu():
    print("""
🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
██╗      █████╗  ██████╗ ███████╗███╗   ██╗
██║     ██╔══██╗██╔════╝ ██╔════╝████╗  ██║
██║     ███████║██║  ███╗█████╗  ██╔██╗ ██║
██║     ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║
███████╗██║  ██║╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """)


def md5_hash(text):
    """Generate MD5 hash for the given text."""
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()

def base64_decode(encoded_text):
    """Decode a Base64 encoded text."""
    import base64
    return base64.b64decode(encoded_text).decode('utf-8')

def generate_jwt_token(payload, secret_key, algorithm='HS256'):
    """Generate a JWT token with the given payload, secret key, and algorithm."""
    import jwt
    return jwt.encode(payload, secret_key, algorithm=algorithm).decode('utf-8')

def decode_md5_hash(md5_hash):
    """Decode an MD5 hash by looking it up in an online database."""
    url = f'https://api.md5hashdatabase.org/{md5_hash}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('text', 'Hash not found in database')
    else:
        return 'Error querying hash database'
