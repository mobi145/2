alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz "

a=input("message:")

key=int(input("key="))

def encrypt(text, key):
    result=[]
    for i in text:
        index = alphabet.index(i)
        new_index = (index + (key*2)) % len(alphabet)
        result.append(alphabet[new_index])

    return "".join(result)

encrypted_message=encrypt(a, key)
print(encrypted_message)

with open("encrypted.txt", "w", encoding="utf-8") as f:
    f.write(encrypted_message)