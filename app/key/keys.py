from cryptography.fernet import Fernet
import base64


def generate_symmetric_key() -> bytes:
    key = Fernet.generate_key()
    encoded_key = base64.urlsafe_b64encode(key)
    with open('key/sql_master_key.txt', 'wb') as f:
        f.write(encoded_key)
    return key


def read_key() -> bytes:
    with open(r'F:\Coding\Iris_V2\app\key\sql_master_key.txt', 'rb') as f:
        key = f.read()
    decoded_key = base64.urlsafe_b64decode(key)
    return decoded_key


def encrypt_message(message: str) -> bytes:
    fernet = Fernet(read_key())
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message: bytes) -> str:
    fernet = Fernet(read_key())
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == '__main__':
    key = generate_symmetric_key()
