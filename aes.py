from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES, Blowfish, ChaCha20
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import messagebox as messagebox
import base64
def encrypt(verbose):
    try:
            if verbose:
                messagebox.create_space_info("Decrypting with AES", write=write_output, print2=not_silence)
                messagebox.space(f"Decrypting message: '{message_decrypt}' with key: '{key.decode()}'", write=write_output, print2=not_silence)
            encrypted_message = base64.b64decode(message_decrypt)
            iv = encrypted_message[:AES.block_size]
            ct = encrypted_message[AES.block_size:]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
            if verbose:
                messagebox.end_space(f"The message was successfully decrypted!", write=write_output, print2=not_silence)
            messagebox.info(f"Decrypted Message: '{plaintext}'", write=write_output, print2=True)

            if save_decrypt:
                messagebox.info(f"Writing Decrypted Message to: '{save_decrypt_file}'", write=write_output, print2=not_silence)
                with open(save_decrypt_file, "a") as fi:
                    fi.write(plaintext)
                    if verbose:
                        messagebox.info("Written to file", write=write_output, print2=not_silence)
    except Exception as e:
            messagebox.error(e)