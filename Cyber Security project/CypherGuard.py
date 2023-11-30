import streamlit as st

def machine(message, mode):
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]

    encrypt_dict = dict(zip(keys, values))
    decrypt_dict = dict(zip(values, keys))

    if mode.lower() == 'encode':
        new_message = ''.join([encrypt_dict[letter] for letter in message.lower()])
    elif mode.lower() == 'decode':
        new_message = ''.join([decrypt_dict[letter] for letter in message.lower()])
    else:
        return "Please try again, wrong choice entered"

    return new_message.capitalize()

st.title("Encryption/Decryption Machine")

message = st.text_input("Enter your secret message:")
mode = st.radio("Crypto Mode:", ('Encode', 'Decode'))

if st.button("Submit"):
    result = machine(message, mode)
    st.success(f"Result: {result}")
