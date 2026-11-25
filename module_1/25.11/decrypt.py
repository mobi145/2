alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz "

with open("encrypted.txt", "r", encoding="utf-8") as f:
    encrypted_text = f.read()


def decrypt(text, key):
    result = []
    for i in text:
        index = alphabet.index(i)
        new_index = (index - (key * 2)) % len(alphabet)
        result.append(alphabet[new_index])

    return "".join(result)

key = int(input("key="))

print(decrypt(encrypted_text, key))