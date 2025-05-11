import streamlit as st
from cryptography.fernet import Fernet

# Generate a new key
def generate_key():
    return Fernet.generate_key()

# Encrypt the message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

# Decrypt the message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()

# Streamlit UI
st.title("🔐 Data Secure Encryption System")

option = st.radio("Choose an option:", ["Generate Key", "Encrypt Data", "Decrypt Data"])

if option == "Generate Key":
    key = generate_key()
    st.code(key.decode(), language='text')
    st.success("🔑 Copy and save this key securely. You'll need it for decryption.")

elif option == "Encrypt Data":
    key = st.text_input("🔑 Enter your encryption key:")
    message = st.text_area("📝 Enter the message to encrypt:")
    if st.button("Encrypt"):
        try:
            encrypted = encrypt_message(message, key.encode())
            st.code(encrypted, language='text')
        except Exception as e:
            st.error(f"Encryption failed: {e}")

elif option == "Decrypt Data":
    key = st.text_input("🔑 Enter your encryption key:")
    encrypted_message = st.text_area("🔒 Enter the encrypted message:")
    if st.button("Decrypt"):
        try:
            decrypted = decrypt_message(encrypted_message, key.encode())
            st.code(decrypted, language='text')
        except Exception as e:
            st.error(f"Decryption failed: {e}")
