def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            result += char  
    return result


message = input("Enter the message: ")
shift_value = int(input("Enter shift value (1-25): "))
choice = input("Choose mode - encrypt or decrypt: ").strip().lower()

if choice in ["encrypt", "decrypt"]:
    output = caesar_cipher(message, shift_value, choice)
    print(f"Result: {output}")
else:
    print("Invalid choice! Please select 'encrypt' or 'decrypt'.")
